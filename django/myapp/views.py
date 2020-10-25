from django.shortcuts import render
from django.views.generic import ListView

from myapp.models import RankId, RecoData

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .renders import MovieJSONRenderer
from .serializers import RecoSerializer, RankSerializer

import pandas as pd
import numpy as np

# ユーザーが評価した映画情報をadminに表示
class RecoDataViewSet(viewsets.ModelViewSet):
  serializer_class = RecoSerializer
  queryset = RecoData.objects.all()

# ユーザー同士がどれだけ似ているかを求める(相関係数を求める)
def get_correlation_coefficents(scores, target_user_index):
  similarities = []
  target = scores[target_user_index]

  for i, score in enumerate(scores):
      indices = np.where(((target + 1) * (score + 1)) != 0)[0]
      # 比較対象が「共通の評価した映画が3つ未満」か「予測対象者自身の場合」、この処理を実行しない
      if len(indices) < 1 or i == target_user_index:
          continue
      # 相関係数を求める
      similarity = np.corrcoef(target[indices], score[indices])[0, 1]
      if np.isnan(similarity): # 相関関係が欠損値の場合、この処理を実行しない
          continue
      # 各ユーザーに対しての相関係数をまとめる
      similarities.append((i, similarity))
  return sorted(similarities, key=lambda s: s[1], reverse=True) # 相関関係の高い順に並べ替える

# 評価値の予測モデル
def predict(scores, similarities, target_user_index, target_item_index):
  target = scores[target_user_index] # 予測対象のユーザーの評価した映画

  avg_target = np.mean(target[np.where(target >= 0)]) # 0以上の評価値の平均

  numerator = 0.0
  denominator = 0.0
  k = 0

  for similarity in similarities:
      # 相関係数の高い順に5人までのユーザーを比較対象とする
      if k > 5 or similarity[1] <= 0.0:
          break
      
      score = scores[similarity[0]]
      # 評価式
      if score[target_item_index] >= 0:
          denominator += similarity[1]
          numerator += similarity[1] * (score[target_item_index] - np.mean(score[np.where(score >= 0)]))
          k += 1

  return  avg_target + (numerator / denominator) if denominator > 0 else -1

# 上のpredictを用いて、予測対象者が評価していない映画の評価値を予測する
def rank_items(scores, similarities, target_user_index):
  rankings = []
  target = scores[target_user_index]
  
  for i in range(scores.shape[1]):
      if target[i] > 0:
          continue
      rankings.append([i, predict(scores, similarities, target_user_index, i)])
  return  sorted(rankings, key=lambda r: r[1], reverse=True)

# Nuxt.jsに送信するAPIの結果
class RecoMovieApi(ListAPIView):
  # 全ユーザーデータをデータベースからクエリセットで読み込む
  user_data = RecoData.objects.all()
  
  # クエリセットをデータフレームに変換する
  df = pd.DataFrame(list(user_data.values()))

  # 不要な行のデータ(id)を除外する
  df = df.drop(columns='id')
  
  # 扱いやすい形にデータを整える(欠損値:評価なしの部分に-1を入れる)
  movie_pivot = df.pivot(index= 'user_id', columns= 'movie_id', values= 'rate').fillna(-1)
  
  # numpy配列に変換する
  scores = np.array(movie_pivot)

  # 対象のユーザーid -1 (※ユーザーidが1から始まっている場合、-1する)
  user_id = 'pvs03WID7AQ2cVzcgjvZ5SuKJtT2'
  user_index = len(movie_pivot[:user_id])
  target_user_index = user_index -1
  
  # 相関係数を求める
  similarities = get_correlation_coefficents(scores, target_user_index)

  # おすすめの映画の列を出力
  rank_c = rank_items(scores, similarities, target_user_index)
  rank_c = np.array(rank_c, dtype=int)
  rank_c = rank_c[: , 0]

  # 出力された列から映画のIDを抽出する
  rank = []
  for i in rank_c:
    a = movie_pivot.columns.values[i]
    rank = np.append(rank, a)

  # 上位3つのおすすめを出力する(足りない場合はその分だけ0を返す)
  if len(rank) < 3:
    zero = np.zeros(3 - len(rank))
    rank = np.r_[rank, zero]
  rank = np.array(rank, dtype=int)

  # RankIdのモデルで定義されたデータに結果を追加する(古いおすすめは消す)
  RankId.objects.all().delete()
  RankId.objects.create(rank1=rank[0],rank2=rank[1],rank3=rank[2])

  # APIの結果(json形式)
  model = RankId
  queryset = RankId.objects.all() # Nuxt.jsに渡すデータ
  renderer_classes = (MovieJSONRenderer, )
  serializer_class = RankSerializer
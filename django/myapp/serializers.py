from rest_framework import serializers
from .models import MovieReview, rank_id
from .models import MovieReview, rank_id

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = MovieReview
    fields = '__all__'

class RankSerializer(serializers.ModelSerializer):
  class Meta:
    model = rank_id
    fields = ('rank1','rank2','rank3')
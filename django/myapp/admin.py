from django.contrib import admin
from .models import RankId, RecoData #作成したモデルをimport

# 作成したモデルを追記
admin.site.register(RankId)
admin.site.register(RecoData)
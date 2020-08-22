from django.contrib import admin
from .models import reco, rank_id #作成したモデルをimport

# 作成したモデルを追記
admin.site.register(reco)
admin.site.register(rank_id)
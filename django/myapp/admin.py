from django.contrib import admin
from .models import Person_data, reco,  rank_id#作成したモデルをimport

# Register your models here.
admin.site.register(Person_data) #作成したモデルを追記

admin.site.register(reco)
admin.site.register(rank_id)
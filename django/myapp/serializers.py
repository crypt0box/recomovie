from rest_framework import serializers
from .models import RecoData, RankId

class RecoSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecoData
    fields = '__all__'

class RankSerializer(serializers.ModelSerializer):
  class Meta:
    model = RankId
    fields = ('rank1','rank2','rank3')
from rest_framework import serializers
from .models import rank_id

class RankSerializer(serializers.ModelSerializer):
  class Meta:
    model = rank_id
    fields = ('rank1','rank2','rank3')
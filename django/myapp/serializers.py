from rest_framework import serializers
from .models import Person_data, rank_id

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person_data
        fields = '__all__' 

class RankSerializer(serializers.ModelSerializer):
  class Meta:
    model = rank_id
    fields = ('rank1','rank2','rank3')
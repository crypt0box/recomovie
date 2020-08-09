from rest_framework import serializers
from .models import Person_data

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person_data
        fields = '__all__' 
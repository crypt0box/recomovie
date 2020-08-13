from django.shortcuts import render
from django.views.generic import ListView

from myapp.models import Person_data

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .renderers import PersonJSONRenderer
from .serializers import PersonSerializer

# Create your views here.

class PersonListApiView(ListAPIView):
    model = Person_data # モデルを指定
    queryset = Person_data.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (PersonJSONRenderer, ) # Rendererを指定
    serializer_class = PersonSerializer # Serializerを指定

class PersonDataViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person_data.objects.all()

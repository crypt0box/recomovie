from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecoMovieApi

# router = DefaultRouter()
# router.register(r"persondata", PersonDataViewSet)

urlpatterns = [
   path('reco/', RecoMovieApi.as_view()),
]
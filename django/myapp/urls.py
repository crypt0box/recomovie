from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecoDataViewSet, RecoMovieApi


router = DefaultRouter()
router.register(r"movie_review", RecoDataViewSet)

urlpatterns = [
   path("", include(router.urls)),
   path('reco/', RecoMovieApi.as_view()),
]
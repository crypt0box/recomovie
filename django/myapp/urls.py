from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import MovieReviewDataViewSet, RecoMovieApi
from .views import MovieReviewDataViewSet

router = DefaultRouter()
router.register(r"movie_review", MovieReviewDataViewSet)

urlpatterns = [
   path("", include(router.urls)),
   # path('reco/', RecoMovieApi.as_view()),
]
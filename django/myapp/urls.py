from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonListApiView
from .views import PersonDataViewSet
from .views import RecoMovieApi

router = DefaultRouter()
router.register(r"persondata", PersonDataViewSet)

urlpatterns = [
    path('get_person/', PersonListApiView.as_view()),
    path("", include(router.urls)),
    path('reco/', RecoMovieApi.as_view()),
]
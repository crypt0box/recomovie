from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonListApiView
from .views import PersonDataViewSet

router = DefaultRouter()
router.register(r"persondata", PersonDataViewSet)

urlpatterns = [
    path('get_person/', PersonListApiView.as_view()),
    path("", include(router.urls)),
]
from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import PersonViewSet

router = DefaultRouter()
router.register(
    "personvs", PersonViewSet
)

from . import views



urlpatterns = [] + router.urls

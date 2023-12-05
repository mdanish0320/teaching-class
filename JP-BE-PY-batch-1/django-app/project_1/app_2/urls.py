from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import PersonModelViewSet

router = DefaultRouter()
router.register(
    "personmvs", PersonModelViewSet
)

urlpatterns = [] + router.urls

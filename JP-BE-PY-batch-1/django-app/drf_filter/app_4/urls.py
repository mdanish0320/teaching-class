from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import PersonModelViewSet_1, PersonModelViewSet_2

router = DefaultRouter()
router.register("mvs/1", PersonModelViewSet_1)
router.register("mvs/2", PersonModelViewSet_2)

urlpatterns = [] + router.urls
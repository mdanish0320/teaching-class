from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import PersonModelViewSet_1, PersonModelViewSet_2

router = DefaultRouter()
router.register("perons/mvs//1", PersonModelViewSet_1, "mvs_1")
router.register("perons/mvs//2", PersonModelViewSet_2, "mvs_2")

urlpatterns = [] + router.urls
from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import PersonModelViewSet
from . views import PersonViewSet

router = DefaultRouter()
router.register("personmvs", PersonModelViewSet, "person_mvs")
router.register("personvs", PersonViewSet, "person_vs")

urlpatterns = [] + router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.category import CategoryModelViewSet
from .views.post import PostModelViewSet


router = DefaultRouter()
router.register("category", CategoryModelViewSet, "category-app")
router.register("post", PostModelViewSet, "post-app")


urlpatterns = [] + router.urls

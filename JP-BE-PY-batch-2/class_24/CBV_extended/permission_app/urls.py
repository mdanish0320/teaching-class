from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.category import CategoryModelViewSet
from .views.post import PostModelViewSet
from .views.user import UserModelViewSet


router = DefaultRouter()
router.register("category", CategoryModelViewSet, "category-permission")
router.register("post", PostModelViewSet, "post-permission")
router.register("user", UserModelViewSet, "user-permission")

urlpatterns = [] + router.urls

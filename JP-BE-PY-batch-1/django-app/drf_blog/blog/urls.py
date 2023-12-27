from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("author/mvs", views.Authormvs)
router.register("post/mvs", views.Postmvs)

urlpatterns = [] + router.urls
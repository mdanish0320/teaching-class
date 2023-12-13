from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("actor/mvs", views.Actormvs)
router.register("movie/mvs", views.Moviemvs)



urlpatterns = [] + router.urls
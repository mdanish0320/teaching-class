from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
  "mvs_filter_1", views.PersonModelViewsSetSearch_1
)
router.register(
  "mvs_filter_2", views.PersonModelViewsSetSearch_2
)

router.register(
  "mvs_filter_3", views.PersonModelViewsSetSearch_3
)

urlpatterns = [] + router.urls
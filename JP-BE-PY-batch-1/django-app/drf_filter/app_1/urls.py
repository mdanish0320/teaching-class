from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
  "mvs_filter_1", views.PersonModelViewsSetSearch_1, "mvs_filter_1"
)
router.register(
  "mvs_filter_2", views.PersonModelViewsSetSearch_2, "mvs_filter_2"
)

router.register(
  "mvs_filter_3", views.PersonModelViewsSetSearch_3, "mvs_filter_3"
)

router.register(
  "mvs_filter_4", views.PersonModelViewsSetSearch_4_diff, "mvs_filter_4"
)

urlpatterns = [] + router.urls
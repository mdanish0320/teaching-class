from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("employee/mvs", views.Employeemvs)
router.register("project/mvs", views.Projectmvs)

urlpatterns = [] + router.urls
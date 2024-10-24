from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.category import CategoryModelViewSet
from .views.product import ProductModelViewSet
from .views.supplier import SupplierListCreateAPI, SupplierRetrieveUpdateDestroyAPIView


router = DefaultRouter()
router.register("category", CategoryModelViewSet)
router.register("product", ProductModelViewSet)

urlpatterns = [
    path("suppliers/", SupplierListCreateAPI.as_view()),
    path("suppliers/<int:pk>", SupplierRetrieveUpdateDestroyAPIView.as_view()),
] + router.urls

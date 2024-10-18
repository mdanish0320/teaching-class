from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.category import CategoryViewSet, CategoryMethodOverrideViewSet

from .views.supplier import (
    SupplierRetrieveUpdateDestroyAPIView,
    SupplierListCreateAPIView,
    SupplierAllViews,
    SupplierMethodOverrideListCreateAPIView,
    SupplierMethodOverrideRetrieveUpdateDestroyAPIView,
)
from .views.product import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("categories-override", CategoryMethodOverrideViewSet)

urlpatterns = [
    path("suppliers/", SupplierListCreateAPIView.as_view()),
    path("suppliers/<int:pk>", SupplierRetrieveUpdateDestroyAPIView.as_view()),
    # all common override methods
    path("suppliers-override/", SupplierMethodOverrideListCreateAPIView.as_view()),
    path(
        "suppliers-override/<int:pk>",
        SupplierMethodOverrideRetrieveUpdateDestroyAPIView.as_view(),
    ),
    # detail view will not work properly. You will need atleast 2 separate classes as above
    path("suppliers-one-class/", SupplierAllViews.as_view()),
    path("suppliers-one-class/<int:pk>", SupplierAllViews.as_view()),
] + router.urls

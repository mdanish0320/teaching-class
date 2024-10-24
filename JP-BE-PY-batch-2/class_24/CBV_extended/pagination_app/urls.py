from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.category import CategoryModelViewSet
from .views.product import ProductModelViewSet
from .views.supplier import SupplierModelViewSet


router = DefaultRouter()
router.register("category", CategoryModelViewSet, "category-pagination")
router.register("product", ProductModelViewSet, "product-pagination")
router.register("supplier", SupplierModelViewSet, "supplier-pagination")

urlpatterns = [] + router.urls

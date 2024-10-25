from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.category import CategoryModelViewSet
from .views.product import ProductModelViewSet
from .views.supplier import SupplierModelViewSet


router = DefaultRouter()
router.register("category", CategoryModelViewSet, "category-app")
router.register("product", ProductModelViewSet, "product-app")
router.register("supplier", SupplierModelViewSet, "supplier-app")

urlpatterns = [] + router.urls

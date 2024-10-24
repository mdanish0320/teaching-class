from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.category import CategoryModelViewSet
from .views.product import ProductModelViewSet
from .views.supplier import SupplierModelViewSet


router = DefaultRouter()
router.register("category", CategoryModelViewSet, "category-adv-filter")
router.register("product", ProductModelViewSet, "product-adv-filter")
router.register("supplier", SupplierModelViewSet, "supplier-adv-filter")

urlpatterns = [] + router.urls

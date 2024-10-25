from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from .views.category import CategoryModelViewSet
from .views.product import ProductModelViewSet
from .views.supplier import SupplierModelViewSet


router = DefaultRouter()
router.register("category", CategoryModelViewSet, "category-file")
router.register("product", ProductModelViewSet, "product-file")
router.register("supplier", SupplierModelViewSet, "supplier-file")

urlpatterns = [] + router.urls

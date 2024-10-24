from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Product
from app.serializers import ProductSerialzer
from ..filters import ProductFilter


# Create your views here.
class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerialzer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

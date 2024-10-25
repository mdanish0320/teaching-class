from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerialzer

from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions


# Create your views here.
class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerialzer
    permission_classes = [DjangoModelPermissions, DjangoObjectPermissions]
    

from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerialzer


# Create your views here.
class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerialzer

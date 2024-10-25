from rest_framework.viewsets import ModelViewSet
from app.models import Product
from ..serializers import ProductSerialzer
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerialzer
    parser_classes = (MultiPartParser, FormParser)  # Handles file uploads

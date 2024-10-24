from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerialzer
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5  # Customize page size for this view
    page_size_query_param = "page_size"
    max_page_size = 100


# Create your views here.
class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerialzer
    pagination_class = CustomPagination

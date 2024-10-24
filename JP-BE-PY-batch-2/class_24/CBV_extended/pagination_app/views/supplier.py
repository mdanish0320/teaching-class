from rest_framework.viewsets import ModelViewSet
from app.models import Supplier
from app.serializers import SupplierSerialzer
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5  # Customize page size for this view
    page_size_query_param = "page_size"
    max_page_size = 100


class SupplierModelViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerialzer
    pagination_class = CustomPagination

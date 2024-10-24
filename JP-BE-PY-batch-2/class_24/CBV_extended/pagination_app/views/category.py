from rest_framework.viewsets import ModelViewSet
from app.models import Category
from app.serializers import CategorySerialzer

from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5  # Customize page size for this view
    page_size_query_param = "page_size"
    max_page_size = 100


# Create your views here.
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer
    pagination_class = CustomPagination

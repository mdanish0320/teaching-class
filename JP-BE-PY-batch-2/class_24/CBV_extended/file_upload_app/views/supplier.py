from rest_framework.viewsets import ModelViewSet
from app.models import Category
from app.serializers import CategorySerialzer


# Create your views here.
class SupplierModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

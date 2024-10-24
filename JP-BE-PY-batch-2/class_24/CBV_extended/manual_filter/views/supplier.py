from rest_framework.viewsets import ModelViewSet
from app.models import Supplier
from app.serializers import SupplierSerialzer


# Create your views here.
class SupplierModelViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerialzer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import Supplier
from app.serializers import SupplierSerialzer


class SupplierListCreateAPI(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerialzer


class SupplierRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerialzer

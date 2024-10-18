from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from app_mvs.models import Supplier
from app_mvs.serializers import SupplierSerializer
from rest_framework.response import Response


class SupplierListCreateAPIView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        print("GET SupplierListCreateAPIView")
        return super().get(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        print("supplier modelviewset list api")
        supplier = self.get_queryset()
        supplier_serializer = self.serializer_class
        serializer = supplier_serializer(supplier, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print("supplier ListCreateAPIView create api")
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print("supplier ListCreateAPIView perform_create api")
        print("serializer.validated_data", serializer.validated_data)

        # here you could pop other table related data
        # save it with your custom logic

        return super().perform_create(serializer)

        # you can also send email after perform_create


class SupplierRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


# detail view will not work properly
class SupplierAllViews(
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierMethodOverrideListCreateAPIView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        print("GET SupplierMethodOverrideListCreateAPIView")
        return super().get(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        print("list SupplierMethodOverrideListCreateAPIView")
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("post SupplierMethodOverrideListCreateAPIView")
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("create SupplierMethodOverrideListCreateAPIView")
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print("perform_create SupplierMethodOverrideListCreateAPIView")
        return super().perform_create(serializer)

    def get_queryset(self):
        print("get_queryset SupplierMethodOverrideListCreateAPIView")
        return super().get_queryset()

    def filter_queryset(self, queryset):
        print("filter_queryset SupplierMethodOverrideListCreateAPIView")
        return super().filter_queryset(queryset)

    # this will only get invoked on single object API
    def get_object(self):
        print("get_object SupplierMethodOverrideListCreateAPIView")
        return super().get_object()

    def get_serializer_class(self):
        print("get_serializer_class SupplierMethodOverrideListCreateAPIView")
        return super().get_serializer_class()

    # this doesn't exits in generics
    # def get_pagination_class():
    #     pass


class SupplierMethodOverrideRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        print("get SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().get(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("retrieve SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("put SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().put(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print("update SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("patch SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().patch(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        print("partial_update SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("delete SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().delete(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        print("destroy SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        print("perform_destroy SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().perform_destroy(instance)

    def perform_update(self, serializer):
        print("perform_update SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().perform_update(serializer)

    def get_queryset(self):
        print("get_queryset SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().get_queryset()

    def filter_queryset(self, queryset):
        print("filter_queryset SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().filter_queryset(queryset)

    # this will only get invoked on single object API
    def get_object(self):
        print("get_object SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().get_object()

    def get_serializer_class(self):
        print("get_serializer_class SupplierMethodOverrideRetrieveUpdateDestroyAPIView")
        return super().get_serializer_class()

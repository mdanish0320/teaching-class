from django.shortcuts import render

# from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Category, Supplier, Product
from .serializers import CategorySerialzer, SupplierSerialzer, ProductSerialzer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

    # http://localhost:8000/app/category/recent
    @action(detail=False, methods=['get'])
    def recent(self, request):
        category_model = self.queryset # Category.objects.all()
        category_serialzer = self.get_serializer(category_model, many=True) # CategorySerialzer
        
        return Response(category_serialzer.data)

    # http://localhost:8000/app/category/1/special        
    @action(detail=True, methods=["get"])
    def special(self, request, pk=None):
        category = self.get_object()
        serializer = self.get_serializer(category)
        return Response(serializer.data)




class SupplierListCreateAPI(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerialzer   


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)


class SupplierRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerialzer  


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.select_related("category").prefetch_related("supplier").all()
    serializer_class = ProductSerialzer  


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        print("create")
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        print("perform create")
        return super().perform_create(serializer)


    # def perform_create(self, serializer):
    #     print("ProductModelViewSet: perform_create")
    #     print("validated_data", serializer.validated_data)

    #     category_id = serializer.validated_data.pop("category_id")
    #     supplier_id = serializer.validated_data.pop("supplier_id")

    #     category_obj = Category.objects.get(pk=category_id)
    #     supplier_obj = Supplier.objects.get(pk=supplier_id)

    #     product = Product.objects.create(**serializer.validated_data, category=category_obj)
    #     product.supplier.set([supplier_obj])

    #     serialzier = ProductSerialzer(product)

    #     return Response(serialzier.data)
    #     # return super().perform_create(serializer)

    # Product.objects.create(**validated_data) # supplier_id, category_id


    # def perform_create(self, serializer):
    #     print("ProductModelViewSet: perform_create")
    #     print("validated_data", serializer.validated_data)

    #     serializer = CategorySerialzer(data=request.data)
    #     if serializer.is_valid():
    #         # Category.objects
    #         serializer.save()

    #     serializer.save()

    #     # category_id = serializer.validated_data.pop("category_id")
        # supplier_id = serializer.validated_data.pop("supplier_id")

        # category_obj = Category.objects.get(pk=category_id)
        # supplier_obj = Supplier.objects.get(pk=supplier_id)

        # product = Product.objects.create(**serializer.validated_data, category=category_obj)
        # product.supplier.set([supplier_obj])

        # serialzier = ProductSerialzer(product)

        # return Response(serialzier.data)
        # return super().perform_create(serializer)
    
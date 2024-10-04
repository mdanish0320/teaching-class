from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Product as product_model, Category as category_model
from .serializers import ProductSerializer, CategoryReverseProductSerializer


@api_view(['GET', 'POST'])
def get_products_or_create_products(requst: Request):
    if requst.method == 'GET':
        params = requst.query_params
        
        products_objects = product_model.objects
        if params.get("name") is not None:
            products_objects = products_objects.filter(name=params.get("name"))

        if params.get("id") is not None:
            products_objects = products_objects.filter(id=params.get("id"))

        products = products_objects.select_related("category").all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if requst.method == 'POST':
        
        serializer = ProductSerializer(data=requst.data)
        print("Before serialization:", serializer.initial_data)
        if serializer.is_valid():
            print("after validation:", serializer.validated_data)
            category =category_model.objects.get(pk=serializer.validated_data['category_id'])
            product_model.objects.create(category=category, **serializer.validated_data)
            
            return Response("success", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_product(requst: Request, id):
    data = {}
    category = product_model.objects.get(pk=id)
    if requst.method == 'GET':
        serializer = ProductSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if requst.method == 'PUT':
        serializer = ProductSerializer(data=requst.data)
        if serializer.is_valid():
            # Loop through all fields in validated_data and update the instance
            for key, value in serializer.validated_data.items():
                setattr(category, key, value)
            category.save()
            serializer = ProductSerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if requst.method == 'DELETE':
        category.delete()
        data = "deleted"

    return Response(data, status=status.HTTP_200_OK)



@api_view(['GET'])
def reverse_category(requst: Request):
    if requst.method == 'GET':
        # the name insdie prefetch_related 'category' is mentioned in models
        # its called related_name
        # lazy_loading = product_model.objects.all()
        # for product in lazy_loading:
        #     product.category


        categories = category_model.objects.prefetch_related('category').all()
        serializer = CategoryReverseProductSerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response("success")
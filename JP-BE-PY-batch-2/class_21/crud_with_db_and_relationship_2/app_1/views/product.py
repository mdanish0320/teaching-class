from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from app_1.models.product import Product as product_model
from app_1.models.category import Category as category_model
from app_1.serializers.product import ProductSerializer, ProductCategorySerializer

"""
input
{
"name": "product 10",
"category_ids": [1]
}
"""
@api_view(['GET', 'POST'])
def create_or_get_customers(requst: Request):
    if requst.method == 'GET':
        
        customers = product_model.objects.all()
        serializer = ProductSerializer(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if requst.method == 'POST':
        
        serializer = ProductSerializer(data=requst.data)
        if serializer.is_valid():
            cat_ids = serializer.validated_data.pop('category_ids')
            
            # custom validation
            # TODO: we could also write this serializer level
            db_categories = category_model.objects.filter(id__in=cat_ids).all()
            if len(db_categories) != len(cat_ids):
                Response("One or more category IDs are invalid.", status=status.HTTP_400_BAD_REQUEST)

            # TODO: variable is a must
            product = product_model.objects.create(**serializer.validated_data)
            product.category.set(cat_ids)
            
            return Response("success", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

"""
input:
{
"product_id": 1,
"category_ids": [1]
}
"""
@api_view(['POST', 'GET'])
def assign_categories(requst: Request):
    
    if requst.method == 'GET':
        # customers = product_model.objects.select_related("category").all() # will not work due to many-to-many relationship
        customers = product_model.objects.prefetch_related("category").all()
        serializer = ProductSerializer(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    serializer = ProductCategorySerializer(data=requst.data)
    if serializer.is_valid():
        product_id = serializer.validated_data.pop('product_id')
        cat_ids = serializer.validated_data.pop('category_ids')
        
        # custom validation
        # TODO: we could also write this serializer level
        db_categories = category_model.objects.filter(id__in=cat_ids).all()
        if len(db_categories) != len(cat_ids):
            return Response("One or more category IDs are invalid.", status=status.HTTP_400_BAD_REQUEST)

        db_product = product_model.objects.filter(id=product_id).first()
        if db_product is None:
            return Response("Invalid product.", status=status.HTTP_400_BAD_REQUEST)

        
        db_product.category.set(cat_ids)
        return Response("success", status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
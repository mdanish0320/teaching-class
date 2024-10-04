from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from django.forms.models import model_to_dict

from .models import ProductWitoutRelation as product_model, Category as category_model


@api_view(['GET', 'POST'])
def get_products_or_create_products(requst: Request):
    if requst.method == 'GET':
        params = requst.query_params
        
        products_objects = product_model.objects
        if params.get("name") is not None:
            products_objects = products_objects.filter(name=params.get("name"))

        if params.get("id") is not None:
            products_objects = products_objects.filter(id=params.get("id"))

        all_data = []
        category_id = products_objects.values_list('category_id', flat=True)
        categories = category_model.objects.filter(id__in=category_id).all()
        products = products_objects.all()
        for product in products:
            for category in categories:
                if product.category_id == category.id:
                    data = {**model_to_dict(product), "category": model_to_dict(category)}
                    all_data.append(data)


        return Response(all_data, status=status.HTTP_200_OK)
    
    if requst.method == 'POST':
        
        data=requst.data
        print(type(data['price']))
        if type(data['name']) is not str or type(data['quantity']) is not int or type(data['price']) is not int or type(data['category_id']) is not int:
            print("invalid data")
            return Response("name, quantity, price and category_id are required", status=status.HTTP_400_BAD_REQUEST)
        
        if len(data['name'].strip()) == 0 or data['quantity'] < 0 or data['price'] <=0 or data['category_id'] < 0:
            return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)

        category = category_model.objects.filter(id=data['category_id']).first()
        if category is None:
            return Response("category not found", status=status.HTTP_400_BAD_REQUEST)
        
        product_model.objects.create(**data)
        
        return Response("success", status=status.HTTP_200_OK)



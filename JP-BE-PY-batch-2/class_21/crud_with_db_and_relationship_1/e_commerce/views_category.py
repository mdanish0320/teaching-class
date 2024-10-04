from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Category as category_model
from .serializers import CategorySerializer


@api_view(['GET', 'POST'])
def get_categories_or_create_category(requst: Request):
    data = []
    if requst.method == 'GET':
        params = requst.query_params
        
        category_objects = category_model.objects
        if params.get("name") is not None:
            category_objects = category_objects.filter(name=params.get("name"))

        if params.get("id") is not None:
            category_objects = category_objects.filter(id=params.get("id"))

        categories = category_objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if requst.method == 'POST':
        
        serializer = CategorySerializer(data=requst.data)
        print("Before serialization:", serializer.initial_data)
        if serializer.is_valid():
            print("after validation:", serializer.validated_data)
            category_model.objects.create(**serializer.validated_data)
            
            return Response("success", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_category(requst: Request, id):
    data = {}
    category = category_model.objects.get(pk=id)
    if requst.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if requst.method == 'PUT':
        serializer = CategorySerializer(data=requst.data)
        if serializer.is_valid():
            # Loop through all fields in validated_data and update the instance
            for key, value in serializer.validated_data.items():
                setattr(category, key, value)
            category.save()
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if requst.method == 'DELETE':
        category.delete()
        data = "deleted"

    return Response(data, status=status.HTTP_200_OK)
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from app_1.models.category import Category as category_model
from app_1.serializers.category import CategorySerializer

@api_view(['GET', 'POST'])
def create_or_get_categories(requst: Request):
    if requst.method == 'GET':
        
        customers = category_model.objects.all()
        serializer = CategorySerializer(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if requst.method == 'POST':
        
        serializer = CategorySerializer(data=requst.data)
        if serializer.is_valid():
            category_model.objects.create(**serializer.validated_data)
            
            return Response("success", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
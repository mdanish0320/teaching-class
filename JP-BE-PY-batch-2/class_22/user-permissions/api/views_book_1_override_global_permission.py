from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Book as book_model
from .serializers import BookSerializer


@api_view(['GET'])
@permission_classes([AllowAny]) # allow accessing this API publically (without auth)
def get_all_books(requst: Request):
    categories = book_model.objects.all()
    serializer = BookSerializer(categories, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
        

@api_view(['POST'])
def create_book(requst: Request): # problem: all logged in user can create posts
    serializer = BookSerializer(data=requst.data)
    if serializer.is_valid():
        data = serializer.validated_data
        data['author_id'] = requst.user.id
        book_model.objects.create(**data)
        return Response("success", status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_book(requst: Request, id):
    
    category = book_model.objects.get(pk=id)
    
    serializer = BookSerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)
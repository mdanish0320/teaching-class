from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PersonModel
from .serializers import PersonSerializer
from rest_framework.request import Request
from rest_framework import status
import json

# Create your views here.
persons = [
    {
        "id": 1,
        "name": "danish"
    },
    {
        "id": 2,
        "name": "fahad"
    },
    {
        "id": 3,
        "name": "shoaib"
    },
    {
        "id": 4,
        "name": "shahzad"
    },

]

@api_view(['GET'])
def get_static_persons(request):
    return Response(persons)



######## Data from DB ##########

@api_view(['GET'])
def get_dynamic_persons(request):
    data = PersonModel.objects.all()
    serialized_person = PersonSerializer(data, many=True)
    return Response(serialized_person.data)


@api_view(['POST'])
def add_dynamic_persons(request:Request):
    serialized_person = PersonSerializer(data=request.data)
    if serialized_person.is_valid():
        serialized_person.save()
    else:
        return Response({"error": "invalid data"}, status.HTTP_400_BAD_REQUEST)
    return Response({"data": {}, "message": "data added"}, status.HTTP_200_OK)


@api_view(['PATCH'])
def update_dynamic_persons(request:Request, id):
    person = PersonModel.objects.get(pk=id)
    # person = PersonModel.objects.filter(name=id).first()
    serialized_person = PersonSerializer(person, data=request.data, partial=True)
    if serialized_person.is_valid(raise_exception=True):
        serialized_person.save()
    else:
        return Response({"error": "invalid data"}, status.HTTP_400_BAD_REQUEST)
    return Response({"data": {}, "message": "data updated"}, status.HTTP_200_OK)


@api_view(['DELETE'])
def update_delete_persons(request:Request, id):
    person = PersonModel.objects.filter(pk=id).first()
    
    if person is None:
        return Response({"error": "person not found"}, status.HTTP_400_BAD_REQUEST)
    
    person.delete()
    return Response({"data": {}, "message": "data deleted"}, status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from app_1.models import PersonModel
from app_1.serializers import PersonSerializer

############### viewsets.ModelViewSet ###############
class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer


############### viewsets.ViewSet ###############
class PersonViewSet(viewsets.ViewSet):
    # it will cache the result
    # queryset = PersonModel.objects.all()
    
    def list(self, request):
        queryset = PersonModel.objects.all()
        serialized_person = PersonSerializer(queryset, many=True)
        return Response(serialized_person.data)
    
    def create(self, request: Request):
        serialized_person = PersonSerializer(data=request.data)
        if serialized_person.is_valid(raise_exception=True):
            serialized_person.save()
        else:
            return Response({"error": "invalid data"}, status.HTTP_400_BAD_REQUEST)
        return Response({"data": {}, "message": "data added"}, status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        person = PersonModel.objects.filter(pk=pk).first()

        if person is None:
            return Response({"error": "person not found"}, status.HTTP_400_BAD_REQUEST)
        
        serialized_person = PersonSerializer(person)
        return Response(serialized_person.data)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
from django.shortcuts import render
from rest_framework.views import APIView
from app_1.models import PersonModel
from rest_framework.response import Response
from rest_framework import status
from app_1.serializers import PersonSerializer

# Create your views here.
class PersonAPIView_1(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        person = PersonModel.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
class PersonAPIView_2(APIView):
    def get(self, request, id):
        person = PersonModel.objects.filter(pk=id).first()
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    def put(self, request, id):
        person = PersonModel.objects.filter(pk=id).first()
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

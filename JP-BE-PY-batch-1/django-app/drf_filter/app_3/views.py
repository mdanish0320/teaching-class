from django.shortcuts import render
from rest_framework.views import APIView
from app_1.models import PersonModel
from rest_framework.response import Response
from rest_framework import status
from app_1.serializers import PersonSerializer

"""
In rest_framework.views.APIView, there is no built-in get_queryset or filter_queryset method. 
These methods are typically associated with views that are based on mixins or generic class-based views that deal with model instances and querysets, 
such as ListAPIView, RetrieveAPIView, or GenericAPIView.

In APIView, which is a more generic view class,
you have the freedom to define your own methods for handling HTTP methods 
(e.g., get, post, put, delete) without the implicit assumptions about querysets and model instances.
"""

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

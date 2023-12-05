from django.shortcuts import render
from rest_framework import viewsets

from app_1.models import PersonModel
from app_1.serializers import PersonSerializer

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
from django.shortcuts import render
from rest_framework import viewsets

from app_1.models import PersonModel
from app_1.serializers import PersonSerializer

############### viewsets.ModelViewSet ###############
class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer



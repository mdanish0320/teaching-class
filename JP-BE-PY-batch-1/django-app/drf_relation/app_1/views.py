from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .serializers import AuthorSerializer, PostSerializer
from .models import AuthorModel, PostModel
from .filters import AuthorFilter


# Create your views here.
class Authormvs(ModelViewSet):
  queryset = AuthorModel.objects.all()
  serializer_class = AuthorSerializer
  
  # filters
  filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
  filterset_class = AuthorFilter
  OrderingFilter = ['fname', 'lname']
  
  
class Postmvs(ModelViewSet):
  queryset = PostModel.objects.all()
  serializer_class = PostSerializer
  
  # use method in serializer
  
  # def create(self, request, *args, **kwargs):
  #   serializer = PostSerializer(data=request.data)
  #   if serializer.is_valid():
  #       serializer.save()
  #   return Response(serializer.data)

  

  


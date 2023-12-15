from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

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

  
  

  


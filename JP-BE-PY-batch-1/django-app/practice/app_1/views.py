from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from .models import MovieModel, ActorModel
from .serializers import MovieSerializer, ActorSerializer
# Create your views here.

class Actormvs(ModelViewSet):
  queryset = ActorModel.objects.all()
  serializer_class = ActorSerializer


class MoviemvsFilter(filters.FilterSet):
  class Meta:
      model = MovieModel
      fields = {
        "title": ['exact', 'contains', 'startswith']
      }
    

  
class Moviemvs(ModelViewSet):
  serializer_class = MovieSerializer
  queryset = MovieModel.objects.all()
  
  # advanced search
  # it will only search with exact data
  filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
  filterset_class = MoviemvsFilter
  ordering_fields = ['title']
  

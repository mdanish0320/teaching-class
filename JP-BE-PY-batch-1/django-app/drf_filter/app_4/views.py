from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from django_filters import NumberFilter
from rest_framework.filters import OrderingFilter

from app_1.models import PersonModel
from app_1.serializers import PersonSerializer
# Create your views here.

class PersonModelViewSet_1(ModelViewSet):
  serializer_class = PersonSerializer
  queryset = PersonModel.objects.all()
  
  # advanced search
  # it will only search with exact data
  filter_backends = [DjangoFilterBackend, OrderingFilter]
  filterset_fields = ['name', 'age'] 
  ordering_fields = ['name']
  # ?name=danish&age=1
  
  
  
  
 # filterset
class PersonFilterSet(FilterSet):
  class Meta:
      model = PersonModel
      # fields = "__all__"
      # fields = ["name"]
      fields = {
        "name": ['exact', 'contains', 'startswith'],
        "age": ['exact', 'gt', 'lt', 'gte'],
      }
  ## custom filter  
  # age = NumberFilter(method='my_custom_filter')
  # def my_custom_filter(self, queryset, age, value):
  #     return queryset.filter(age__gte = value)
      

    
  
class PersonModelViewSet_2(ModelViewSet):
  serializer_class = PersonSerializer
  queryset = PersonModel.objects.all()
  
  # advanced search
  # it will only search with exact data
  filter_backends = [DjangoFilterBackend]
  filterset_class = PersonFilterSet
  # ?name=danish&age=1
  
  # def get_queryset(self):
  #    qs = super().get_queryset()
  #    return qs.filter(age__gte=18)
  
  
  # class PersonFilterSet(FilterSet):
  #   name_contains = CharFilter(field_name='name', lookup_expr='contains')
  #   name_exact = CharFilter(field_name='name', lookup_expr='exact')
  #   age = CharFilter(field_name='age', lookup_expr='exact')

  #   class Meta:
  #       model = PersonModel
  #       fields = ['name_contains','name_exact', 'age']  
  
  
  
  
  
  
  
  

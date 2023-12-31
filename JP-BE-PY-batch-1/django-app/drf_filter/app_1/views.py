from django.shortcuts import render
from .models import PersonModel
from .serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.request import Request

# for filter
from rest_framework import filters

# Create your views here.
class PersonModelViewsSetSearch_1(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    
    # filter
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'age']
    #  search_fields =['^name','=city']
    # ^startswith
    # =exactsearch
    
    ## supports query string i.e
    
    # for name
    #?search=danish
    #?search=dan
    
    # for age
    #?search=1
    #?search=2
    
    
    
class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request: Request):
        name_param = request.query_params.get('name')
        age_param = request.query_params.get('age')

        query_params = []
        if name_param is not None:
          query_params.append('name') # first_hame
          
        if age_param is not None:
          query_params.append('age') # last_name
        
        print("CustomSearchFilter", query_params)
        return query_params
      
class PersonModelViewsSetSearch_2(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
        
    # filter
    filter_backends = [CustomSearchFilter]

    ## supports query string i.e
    # single value specific multiple fields i.e
    # ?search=dans&name=True&age=True
    
    # good for the multi field if searched term is same i.e
    # ?search=danish&fname=True&lname=True
    
    # good for the search result of single field search i.e
    # ?search=Animal&movie_name=True
    
    # Cannot search on multi fields if search terms are different i.e
    # title=Animal&Year=2023
    
  
  
class PersonModelViewsSetSearch_3(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = PersonModel.objects.all()
        name_param = self.request.query_params.get('name')
        age_param = self.request.query_params.get('age')
        
        if name_param:
            queryset = queryset.filter(name=name_param)
        
        if age_param:
            queryset = queryset.filter(age=age_param)
        return queryset
      
  # ?search=Animal&movie_name=True


class PersonModelViewsSetSearch_4_diff(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter]


    # calls before the filter_queryset
    def get_queryset(self):
        print("get_queryset")
        queryset = PersonModel.objects.all()
        name_param = self.request.query_params.get('name')
        if name_param:
            queryset = queryset.filter(name=name_param)
        
        return queryset
  
    # calls after the get_queryset
    def filter_queryset(self, queryset):
        print("filter_queryset")
        # Apply additional custom filtering based on the request
        age_param = self.request.query_params.get('age')
        if age_param:
            queryset = queryset.filter(age=age_param)
        return queryset
    
# filter queryset    
# https://ctrlzblog.com/django-queryset-filter-15-examples/
  

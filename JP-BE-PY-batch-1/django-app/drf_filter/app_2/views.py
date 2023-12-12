from django.shortcuts import render
from rest_framework import generics, mixins
from app_1.models import PersonModel
from rest_framework.response import Response
from rest_framework import status
from app_1.serializers import PersonSerializer
from rest_framework import filters

"""
They consist of GenericAPIView, mixins, and concrete views:

- GenericAPIView is a more loaded version of APIView. It isn't really useful on its own but can be used to create reusable actions.
- Mixins are bits of common behavior. They're useless without GenericAPIView.
- Concrete views combine GenericAPIView with the appropriate mixins to create views often used in APIs.
"""

############## Concrete API View ##################

# Create your views here.
class PersonConcrete_Create_And_List(
    generics.ListAPIView,
    generics.CreateAPIView,
    # generics.UpdateAPIView,
    # generics.DestroyAPIView,
    # generics.RetrieveAPIView
):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'age']
    
    # def get_queryset(self):
    #     return super().get_queryset()
    
    # def filter_queryset(self, queryset):
    #     return super().filter_queryset(queryset)


class PersonConcrete_Read_Update_AND_Delete(
    # generics.ListAPIView,
    # generics.CreateAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.RetrieveAPIView
):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id' # <--- necessary to mention








############## Mixins ##################

class PersonMixin_Create_And_List(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):

    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class PersonMixin_Read_Update_AND_Delete(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id' # <--- necessary to mention

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    



############## GenericAPIView ##################
class PersonGenerics_1(generics.GenericAPIView):

    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class PersonGenerics_2(generics.GenericAPIView):   
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import action

from app_1.models import PersonModel
from app_1.serializers import PersonSerializer

############### viewsets.ModelViewSet ###############
"""
ModelViewSet extends GenericAPIView, you'll normally need to provide at least the queryset and serializer_class
"""
class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer

    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.validated_data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False)
    # def recent_users(self, request):
    #     recent_users = User.objects.all().order_by('-last_login')

    #     page = self.paginate_queryset(recent_users)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(recent_users, many=True)
    #     return Response(serializer.data)


############### viewsets.ViewSet ###############
"""
The ViewSet class does not provide any implementations of actions. 
In order to use a ViewSet class you'll override the class and define the action implementations explicitly.
"""
class PersonViewSet(viewsets.ViewSet):
    # it will cache the result
    # queryset = PersonModel.objects.all()

    def list(self, request):
        queryset = PersonModel.objects.all()
        serialized_person = PersonSerializer(queryset, many=True)
        return Response(serialized_person.data)
    
    def create(self, request: Request):
        serialized_person = PersonSerializer(data=request.data)
        if serialized_person.is_valid(raise_exception=True):
            serialized_person.save()
        else:
            return Response({"error": "invalid data"}, status.HTTP_400_BAD_REQUEST)
        return Response({"data": {}, "message": "data added"}, status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        person = PersonModel.objects.filter(pk=pk).first()

        if person is None:
            return Response({"error": "person not found"}, status.HTTP_400_BAD_REQUEST)
        
        serialized_person = PersonSerializer(person)
        return Response(serialized_person.data)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

# using GenericViewSet, we are customizing the CRUD operations such that we only allow 2 endpoint POST and GET
# furthermore, in POST API we need custom logic before storing data into db.
class PersonGenericViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint for adding and processing new client by uid
    """
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer

    def create(self, request: Request):
        if "uid" in request.data:
            try:
                # it will not work as it is used in /resource/<id> case
                # and that case also expects lookup_field = 'id'
                # self.get_queryset()
                instance = PersonModel.objects.get(pk=request.POST['uid'])
                serializer = PersonModel(
                    instance=instance,
                    data=request.data
                )
            except PersonModel.DoesNotExist:
                serializer = PersonModel(data=request.data)
        else:
            serializer = PersonModel(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

"""
There are four types of ViewSets, from the most basic to the most powerful:
1. ViewSet
2. GenericViewSet
3. ReadOnlyModelViewSet
4. ModelViewSet
"""
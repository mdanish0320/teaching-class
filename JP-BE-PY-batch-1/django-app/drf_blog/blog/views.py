from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .serializers import AuthorSerializer, AuthorListingSerializer, PostSerializer
from .models import AuthorModel, PostModel


# Create your views here.
class Authormvs(ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def __init__(self, *args, **kwargs):
        super(Authormvs, self).__init__(*args, **kwargs)
        self.serializer_action_classes = {
            'list': AuthorListingSerializer,
            'create':AuthorSerializer,
            'retrieve':AuthorListingSerializer,
            'update':AuthorSerializer,
            'partial_update':AuthorSerializer,
            'destroy':AuthorSerializer,
        }

    def get_serializer_class(self, *args, **kwargs):
        """Instantiate the list of serializers per action from class attribute (must be defined)."""
        kwargs['partial'] = True
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(Authormvs, self).get_serializer_class()
  
class Postmvs(ModelViewSet):
  queryset = PostModel.objects.all().order_by('-updated_at')
  serializer_class = PostSerializer
  
  

  


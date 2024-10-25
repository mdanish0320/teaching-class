from rest_framework.viewsets import ModelViewSet
from ..models import Post
from ..serializers import PostSerialzer

from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions


# Create your views here.
class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.select_related("category", "user").all()
    serializer_class = PostSerialzer
    permission_classes = [DjangoModelPermissions, DjangoObjectPermissions]

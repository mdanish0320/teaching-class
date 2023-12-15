from rest_framework import serializers
from .models import AuthorModel, PostModel


class AuthorSerializer(serializers.ModelSerializer):
  # sections = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = AuthorModel
    fields = "__all__"
    
    
class PostSerializer(serializers.ModelSerializer):
  # author = AuthorSerializer(many=True, read_only=True)
  class Meta:
    model = PostModel
    fields = "__all__"
    depth = 1
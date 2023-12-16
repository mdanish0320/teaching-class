from rest_framework import serializers
from .models import AuthorModel, PostModel


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthorModel
    fields = "__all__"
    
    
class PostSerializer(serializers.ModelSerializer):
  # add this field to make author_id available in validated_data
  author_id = serializers.CharField()
  
  class Meta:
    model = PostModel
    fields = "__all__"
    depth = 1
    
  def create(self, validated_data):
    author_id = validated_data.pop("author_id")
    author_model = AuthorModel.objects.filter(id=author_id).first()
    return PostModel.objects.create(**validated_data, author=author_model)

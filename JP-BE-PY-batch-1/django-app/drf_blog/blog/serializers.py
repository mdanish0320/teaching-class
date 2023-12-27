from rest_framework import serializers
from .models import AuthorModel, PostModel
from django.contrib.auth.models import User
from account.serializers import BloggerSerializer

class AuthorListingSerializer(serializers.ModelSerializer):
    user = BloggerSerializer()
    class Meta:
        model = AuthorModel
        fields = ['fname', 'lname', 'user']


class AuthorSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = AuthorModel
        fields = ['fname', 'lname', 'user_id']

    def create(self, validated_data):
        user = User.objects.filter(id=validated_data['user_id']).first()
        if user is None:
           raise serializers.ValidationError(({"user_id": "user doesn't exists with this id"}))
        return AuthorModel.objects.create(**validated_data, user=user)
    
    
class PostSerializer(serializers.ModelSerializer):
    # add this field to make author_id available in validated_data
    author_id = serializers.CharField()

    class Meta:
        model = PostModel
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        user = User.objects.filter(id=validated_data['author_id']).first()
        if user is None:
           raise serializers.ValidationError(({"user_id": "user doesn't exists with this id"}))
        return PostModel.objects.create(**validated_data, author=user)

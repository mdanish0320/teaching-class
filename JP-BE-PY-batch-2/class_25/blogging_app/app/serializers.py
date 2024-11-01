from rest_framework import serializers
from .models import Category, Post
from django.contrib.auth.models import User
from user_auth.serializers import UserSerializer

# class CategorySerialzer(serializers.Serializer):


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerialzer(serializers.ModelSerializer):
    category = CategorySerialzer(read_only=True)
    author = UserSerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        category_obj = validated_data.pop("category_id")
        logged_in_user = self.context["request"].user

        post = Post.objects.create(
            **validated_data, category=category_obj, author=logged_in_user
        )

        return PostSerialzer(post).data

from rest_framework import serializers
from app.models import Category, Supplier, Product
from .models import Post
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm

# class CategorySerialzer(serializers.Serializer):


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerialzer(serializers.ModelSerializer):
    user_type = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), write_only=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "user_type"]


class PostSerialzer(serializers.ModelSerializer):
    category = CategorySerialzer(read_only=True)
    user = UserSerialzer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        category_obj = validated_data.pop("category_id")

        # Get the logged-in user from the context
        logged_in_user = self.context["request"].user

        product = Post.objects.create(
            **validated_data, category=category_obj, user=logged_in_user
        )

        moderator_group = Group.objects.get(
            name="moderator"
        )  # Replace with the actual group name
        author_group = Group.objects.get(
            name="author"
        )  # Replace with the actual group name

        # moderator
        assign_perm("view_post", moderator_group, product)
        assign_perm("change_post", moderator_group, product)

        # author
        assign_perm("view_post", author_group, product)

        # owner
        assign_perm("view_post", logged_in_user, product)
        assign_perm("change_post", logged_in_user, product)
        assign_perm("delete_post", logged_in_user, product)

        serialzier = PostSerialzer(product)

        return serialzier.data

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

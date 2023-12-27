from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    name = serializers.CharField(required=False)

    def validate(self, data):
        # Perform default validation provided by the serializer for all fields
        data = super().validate(data)

        # Add additional custom validation
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Password doesn't match"})

        existing_user = User.objects.filter(username=data['username']).exists()
        if existing_user:
            raise serializers.ValidationError({'username': "username is already in use"})
            
        return data
    
    def create(self, validated_data):
        return User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            is_staff=False,
            is_superuser=False
        )

class AdminRegisterSerializer(serializers.Serializer):
    USER_TYPE = (
        ('moderator', 'Moderator'),
        ('superuser', 'Super User'),
    )
    username = serializers.CharField()
    user_type = serializers.ChoiceField(choices=USER_TYPE)
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        # Perform default validation provided by the serializer for all fields
        data = super().validate(data)

        # Add additional custom validation
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Password doesn't match"})

        existing_user = User.objects.filter(username=data['username']).exists()
        if existing_user:
            raise serializers.ValidationError({'username': "username is already in use"})

        return data
    
    def create(self, validated_data):
        is_staff = True if validated_data['user_type'] == 'moderator' else False
        is_superuser = True if validated_data['user_type'] == 'superuser' else False
        if is_superuser == True:
            is_staff = True
            
        return User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            is_staff=is_staff,
            is_superuser=is_superuser,
        )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

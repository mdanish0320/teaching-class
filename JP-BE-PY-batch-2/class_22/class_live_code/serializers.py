from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    dob = serializers.DateField()
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(read_only=True) 


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
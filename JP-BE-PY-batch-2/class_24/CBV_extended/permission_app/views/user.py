from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User, Group
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

from ..serializers import PostSerialzer, UserSerialzer
from ..permissions import IsSuperUser


# Create your views here.


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
    permission_classes = [IsSuperUser]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # Extract user data from the request
        user_data = request.data

        # Create a new user instance
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            is_staff=1,
        )

        group = user_data.get("user_type")

        # Set the password (this will hash it)
        user.set_password(user_data["password"])
        user.save()
        user.groups.add(group)  # Add user to the group

        return Response(
            {"detail": "User created successfully."}, status=status.HTTP_201_CREATED
        )

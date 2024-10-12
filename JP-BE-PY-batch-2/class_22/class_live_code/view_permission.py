from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import AllowAny


from .serializers import UserSerializer, LoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request: Request):
    data = request.data # json input from user
    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        data['password'] = make_password(data['password'])
        # data['is_staff'] = 1
        # data['is_superuser'] = 1
        User.objects.create(**data)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    return Response("success")
    

# djangoModelPermission
# djangoobjectpermission


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request: Request):
    data = request.data # json input from user
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        
        user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None:
            login(request, user)

            # resp = make_response("success")
            # resp.set_cookie(session_id, str(user_id), expire_at=1000, http_only=True)
            return Response("success")
        else:
            return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request: Request):

    logout(request)
    return Response("success")


from rest_framework.permissions import BasePermission
class IsAuthor(BasePermission):
    """
    Custom permission to allow only users in the 'author' group to create books.
    """
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='author').exists()


@api_view(['GET'])
@permission_classes([IsAuthor])
def profile_view(request: Request):
    
    user = UserSerializer(request.user)
    return Response(user.data)
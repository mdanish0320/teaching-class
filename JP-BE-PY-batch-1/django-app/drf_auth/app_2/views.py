from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission

from app_1.serializers import UserSerializer


# user this permission class to remove the authentication
class PublicEndpointPermission(BasePermission):
    """
    Allow access to any user (unauthenticated users as well).
    """
    def has_permission(self, request, view):
        return True
    
# class is_customer(BasePermission):
#     def has_permission(self, request, view):
#         if request.user and request.user.groups.filter(name='customers'):
#             return True
#         return False


# class is_staff(BasePermission):
#     def has_permission(self, request, view):
#         if request.user and request.user.groups.filter(name='staff'):
#             return True
#         return False





class Usermvs(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # update permission of the list API
    def get_permissions(self):
        if self.action == 'list':
            return [PublicEndpointPermission()]  # Replace with your desired permission class
        return super().get_permissions()

    # detail=True means it will require pk in the URL
    @action(detail=False, methods=['post'], permission_classes=[PublicEndpointPermission])
    def login(self, request):
        if request.user.is_authenticated:
            print("user already loggedin")
            return Response({"error": {"message": "you are already logged in"}})
        
        data = request.data
        username = data['username']
        password = data['password']

        user = User.objects.filter(username=username).first()
        if user is None:
            print("user not found")
            return Response({"error": {"message": "invalid credentials"}})
        
        valid_user = authenticate(username=username, password=password)
        if valid_user is None:
            print("wrong password")
            return Response({"error": {"message": "invalid credentials"}})

        login(user=user, request=request)
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request=request)
        return Response({
            "message": "user is logged out"
        })
    
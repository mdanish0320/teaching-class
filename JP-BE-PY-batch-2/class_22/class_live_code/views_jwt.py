from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import UserSerializer



@api_view(['POST'])
def login_view(request: Request):
    data = request.data # json input from user
    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is not None:
            # login(request, user)
            refresh_token = RefreshToken.for_user(user)
            return Response({
                "refresh_token": str(refresh_token), # expiry 30 days
                "access_token": str(refresh_token.access_token), # expiry 1 day
                
            })
        else:
            return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile_view(request: Request):
    if request.user.is_authenticated:
        user = UserSerializer(request.user)
        return Response(user.data)
    else:
        return Response("please login")


# PASSWORD:
#     SAIMSCS2024



# session_id=1000
# jwt=1000

# headers: {
#   "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4NzIzMDkwLCJpYXQiOjE3Mjg3MjEyOTAsImp0aSI6ImY5ZDg2OTdlY2E0YTRhZTY5ZTk0N2IzNjgyNWY4N2M1IiwidXNlcl9pZCI6NH0.D0KLkrGtbPIgxMiNvIIFcKAqEYtHfr6ORF3jqXLEcKE"
# }
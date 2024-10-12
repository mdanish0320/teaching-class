```python
pip install djangorestframework-simplejwt

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}

#urls.py
from rest_framework_simplejwt.views import TokenRefreshView
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#views.py
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# create user
User.objects.create(
    email="danish@gmail.com", 
    username="danish", 
    password=make_password("admin"),
    is_staff=True,            # Grants access to the admin interface
    is_superuser=True         # Grants all permissions and unrestricted access
)


# Authenticate the user
user = authenticate(request, username=username, password=password)

if user is not None:
    refresh_token = RefreshToken.for_user(user)
    return Response({
        "access_token": str(refresh_token.access_token),
        "refresh_token": str(refresh_token)
        }, status=status.HTTP_200_OK)
```
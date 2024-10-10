### 1. Install Dependencies

First, install the required packages:

```bash
pip install djangorestframework-simplejwt
```

### 2. Configure JWT in Settings

In `myproject/settings.py`, configure DRF to use JWT for authentication:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

Also, configure JWT settings (optional):

```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}
```

### 3. Create URLs for JWT Authentication

In `authapp/urls.py`, define paths for login, token refresh, and logout:

```python
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 4. JWT Authentication Views (FBV)

In `authapp/views.py`, implement the login and logout views. For JWT, we'll use `TokenObtainPairView` to get an access and refresh token.

#### Login View (Using JWT)

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Please provide both username and password."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
```

#### Logout View (Invalidate Token)

For logging out with JWT, you can either store the token on the client-side and remove it upon logout or blacklist the token (requires token blacklisting). Here's a simple approach where we don't blacklist, but just simulate a logout by discarding the tokens client-side:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def logout_view(request):
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
```

### 5. Testing JWT Authentication

You can test these APIs using tools like **Postman** or **curl**.

#### Login Request (Obtain JWT):

```bash
POST /auth/login/
{
  "username": "testuser",
  "password": "testpassword"
}
```

This will return both `access` and `refresh` tokens:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

#### Token Refresh Request (Obtain New Access Token):

```bash
POST /auth/token/refresh/
{
  "refresh": "your_refresh_token"
}
```

This will return a new access token:

```json
{
  "access": "new_access_token"
}
```

#### Logout Request:

```bash
POST /auth/logout/
```

### 6. Securing API Endpoints with JWT

To secure any other API views, ensure you use the `@api_view` decorator and that the JWT tokens are passed in the `Authorization` header in the format:

```
Authorization: Bearer <access_token>
```

For example, to secure an endpoint that returns user details:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def user_detail_view(request):
    user = request.user
    if user.is_authenticated:
        return Response({"username": user.username, "email": user.email}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
```

### 7. Migrate the Database

Run migrations to apply any changes:

```bash
python manage.py migrate
```

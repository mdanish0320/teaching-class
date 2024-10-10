### Configuring Authentication and Permissions in Django REST Framework

In Django REST Framework (DRF), the `REST_FRAMEWORK` setting in `settings.py` allows you to configure important aspects such as **default authentication** and **default permissions**. These settings define how users are authenticated and what permissions are required to access certain API endpoints.

### 1. **Default Authentication**

The `DEFAULT_AUTHENTICATION_CLASSES` setting specifies how the authentication will be handled for requests. DRF supports a wide variety of authentication mechanisms like session-based, token-based, and JWT-based authentication.

#### Syntax:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'your.authentication.class.here',
    ]
}
```

#### Common Authentication Classes:
Here are the most common authentication classes and their impact:

1. **Session Authentication**:
   ```python
   'rest_framework.authentication.SessionAuthentication',
   ```
   - **Impact**: Uses Django's session framework (via cookies) for authentication. It's suitable for browser-based clients.
   - **Use Case**: Standard for websites using Django's default authentication system.

2. **Basic Authentication**:
   ```python
   'rest_framework.authentication.BasicAuthentication',
   ```
   - **Impact**: Uses HTTP Basic Authentication, sending the username and password with every request (in base64 encoding). Not recommended for production use unless using HTTPS.
   - **Use Case**: Quick API testing or internal APIs, often with tools like Postman or cURL.

3. **Token Authentication**:
   ```python
   'rest_framework.authentication.TokenAuthentication',
   ```
   - **Impact**: Clients authenticate by sending a token with each request, typically in the `Authorization` header as `Bearer <token>`. Tokens are issued upon login and stored in a separate table in the database.
   - **Use Case**: For APIs with clients (like mobile apps) that require stateless authentication.

4. **JWT Authentication (using SimpleJWT)**:
   ```python
   'rest_framework_simplejwt.authentication.JWTAuthentication',
   ```
   - **Impact**: Clients authenticate using JWT tokens. JWT (JSON Web Tokens) are self-contained, stateless tokens, often with an **access token** and a **refresh token**. Tokens are passed in the `Authorization` header as `Bearer <token>`.
   - **Use Case**: Modern APIs where stateless, secure token-based authentication is required.

5. **Custom Authentication**:
   You can also define your own authentication class by inheriting from `BaseAuthentication` or other built-in DRF authentication classes.

#### Example of multiple authentication methods:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}
```

#### Impact:
- **Session-based authentication** is suitable for web apps where sessions (cookies) are used.
- **Token-based or JWT-based authentication** is preferred for APIs consumed by mobile apps or third-party clients.

### 2. **Default Permission**

The `DEFAULT_PERMISSION_CLASSES` setting determines the permission policy for the views (i.e., whether the user is allowed to access the API endpoint).

#### Syntax:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'your.permission.class.here',
    ]
}
```

#### Common Permission Classes:

1. **Allow Any**:
   ```python
   'rest_framework.permissions.AllowAny',
   ```
   - **Impact**: No authentication or permission checks are required. Any user, authenticated or not, can access the API.
   - **Use Case**: Public APIs or login endpoints where no authentication is required.

2. **IsAuthenticated**:
   ```python
   'rest_framework.permissions.IsAuthenticated',
   ```
   - **Impact**: Only authenticated users can access the API. Unauthenticated users will receive a `401 Unauthorized` response.
   - **Use Case**: For API endpoints that require logged-in users to access, like profile management.

3. **IsAdminUser**:
   ```python
   'rest_framework.permissions.IsAdminUser',
   ```
   - **Impact**: Only users who are marked as admins (superusers) can access the API. Non-admin users will receive a `403 Forbidden` response.
   - **Use Case**: Admin-specific actions like user management or sensitive operations.

4. **IsAuthenticatedOrReadOnly**:
   ```python
   'rest_framework.permissions.IsAuthenticatedOrReadOnly',
   ```
   - **Impact**: Unauthenticated users can only perform "safe" methods like `GET` (read-only). Authenticated users can perform write operations like `POST`, `PUT`, or `DELETE`.
   - **Use Case**: Public read-only APIs where only authenticated users should be able to make changes.

5. **DjangoModelPermissions**:
   ```python
   'rest_framework.permissions.DjangoModelPermissions',
   ```
   - **Impact**: Permissions are tied to the user's Django model-level permissions (via Django's `User` and `Group` permissions). The user must have the appropriate permissions (e.g., `add`, `change`, `delete`) on the models.
   - **Use Case**: When you want to integrate API access control with Django's built-in model permissions system.

6. **Custom Permissions**:
   You can also define your own permission classes by inheriting from `BasePermission`.

#### Example:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

#### Impact:
- Setting **`AllowAny`** makes the API publicly accessible without any security layer.
- Using **`IsAuthenticated`** requires the user to be authenticated before accessing any API, ensuring security and restricting access to logged-in users.

### Example Configuration:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

- **Authentication**: The user must be either logged in via session or use a JWT token for authentication.
- **Permissions**: Only authenticated users can access any API endpoints. Unauthenticated users will receive a `401 Unauthorized` response.


### Summary:
- `DEFAULT_AUTHENTICATION_CLASSES` controls how users are authenticated (session, basic, token, JWT, etc.).
- `DEFAULT_PERMISSION_CLASSES` controls who can access your API (public, authenticated users, admins, etc.).
- You can combine multiple authentication and permission classes as needed.


### Allowing Public Access to Specific Views

If you want to make certain APIs public while maintaining the default `IsAuthenticated` permission for the rest of your views, you can use the `@permission_classes` decorator with `AllowAny`.

#### Example of Function-Based Views (FBV) with Public and Private Access:

```python
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Public API (no authentication required)
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public API. Anyone can access it."})

# Private API (authentication required)
@api_view(['GET'])
def private_view(request):
    return Response({"message": "You are authenticated. Only authenticated users can access this."})
```

### Explanation:

- **Setting Default Permissions**:
  - By setting `DEFAULT_PERMISSION_CLASSES` to `IsAuthenticated` in `settings.py`, you ensure that all views require authentication by default.

- **Making Views Public**:
  - For the `public_view`, using the `@permission_classes([AllowAny])` decorator overrides the default permissions, allowing any user (authenticated or not) to access this endpoint.
  - The `private_view` remains protected by the default `IsAuthenticated` permission.

### Summary

- **Authentication Configuration**: You can set multiple authentication classes in `DEFAULT_AUTHENTICATION_CLASSES` to manage how users are authenticated.
- **Permissions Configuration**: The default permission can be set to enforce authentication across your API, while specific views can be made public by overriding permissions with the `@permission_classes` decorator.

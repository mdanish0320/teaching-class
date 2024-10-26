# Django Guardian Integration

This guide provides detailed instructions for integrating the **Django Guardian** library, enabling object-level permissions in your Django application.

## Prerequisites

Before proceeding, ensure that you have Django installed and set up in your project.

## Installation

To install the `django-guardian` package, run the following command:

```bash
pip install django-guardian
```

## Configuration

### Update `settings.py`

1. **Add `guardian` to `INSTALLED_APPS`**:

   Open your `settings.py` file and include `guardian` in the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       # Other apps...
       'guardian',
   ]
   ```

2. **Configure Authentication Backends**:

   Modify the `AUTHENTICATION_BACKENDS` setting to include the Guardian backend, allowing for object-level permissions:

   ```python
   AUTHENTICATION_BACKENDS = (
       'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
       'guardian.backends.ObjectPermissionBackend',  # Object-level permissions
   )
   ```

3. **Set `ANONYMOUS_USER_ID`**:

   Specify an ID for anonymous users, enabling them to have permissions:

   ```python
   ANONYMOUS_USER_ID = -1
   ```

## Implementing Object-Level Permissions in Views

### Update `views.py`

```python
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions, DjangoObjectPermissions]
```

## Migrations and Superuser Setup

1. **Run Migrations**:

   Execute the following command to apply migrations for the `guardian` package:

   ```bash
   python manage.py migrate
   ```

2. **Create a Superuser**:

   To access the admin interface, create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

## Assigning Object-Level Permissions

You can dynamically assign object-level permissions to users or groups. Below is an example:

```python
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import User, Group

# Assign object-level permissions for a specific user
user = User.objects.get(username='username')  # Replace with the actual username
assign_perm('view_product', user, product)
assign_perm('change_product', user, product)
assign_perm('delete_product', user, product)

# Assign object-level permissions for a group
group = Group.objects.get(name='Product Managers')  # Replace with the actual group name
assign_perm('view_product', group, product)
assign_perm('change_product', group, product)
assign_perm('delete_product', group, product)
```

## Applying Object-Level Permissions in the Admin Interface

To enforce object-level permissions in the Django admin interface, modify `admin.py` as follows:

```python
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Product

class ProductAdmin(GuardedModelAdmin):
    def has_view_permission(self, request, obj=None):
        """Check if the user has view permission at the object level."""
        if obj is not None:
            return request.user.has_perm('view_product', obj)
        return super().has_view_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        """Check if the user has change permission at the object level."""
        if obj is not None:
            return request.user.has_perm('change_product', obj)
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """Check if the user has delete permission at the object level."""
        if obj is not None:
            return request.user.has_perm('delete_product', obj)
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        """Use the regular model-level permission for adding."""
        return super().has_add_permission(request)

admin.site.register(Product, ProductAdmin)
```

### Configuration Dictionary for Permissions

Instead of hardcoding group permissions in your `create` method, consider using a configuration dictionary. This approach allows you to define roles and their associated permissions more flexibly, making it easier to update permissions without altering core logic.

```python
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import User, Group

# Define permissions in a configuration dictionary
PERMISSIONS_CONFIG = {
    "moderator": ["view_post", "change_post"],
    "author": ["view_post"],
}

def create(self, validated_data):
    ...
    # Assign permissions based on the configuration
    for group_name, permissions in PERMISSIONS_CONFIG.items():
        try:
            group = Group.objects.get(name=group_name)
            for perm in permissions:
                assign_perm(perm, group, product)
        except Group.DoesNotExist:
            print(f"Group {group_name} does not exist.")

    # Assign owner permissions
    assign_perm("view_post", logged_in_user, product)
    assign_perm("change_post", logged_in_user, product)
    assign_perm("delete_post", logged_in_user, product)
```

### Custom Object-Level Permission and View-Level Permission

To implement a custom permission check for object-level permissions, you can define a custom permission class:

```python
from rest_framework import permissions

class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # View level permission
        if request.method in ['GET']:
            return True
        # Only allow POST requests if the user is an admin
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Allow any GET request on the object
        if request.method in ['GET']:
            return True
        # Only allow PUT and DELETE if the user is an admin
        return request.user and request.user.is_staff

class IsAuthor(BasePermission):
    """
    View Level Permssion
    Custom permission to allow only users in the 'author' group to create books.
    """
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='author').exists()  

class IsAuthorOrModerator(BasePermission):
    """
    Custom permission to allow:
    - Authors to delete their own books
    - Moderators to delete any book
    """
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is a moderator
        if request.user.groups.filter(name='moderator').exists():
            return True
        
        # Allow access if the user is the author of the book
        return obj.author_id == request.user.id    
```

### Update to use queryset for listing api `views.py`

Create a `ProductViewSet` that utilizes Django's built-in permissions

```python
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return super().get_queryset().filter(user=user)  # Assuming Product has a ForeignKey to User
        return Product.objects.none()  # Return an empty queryset if the user is not authenticated
```

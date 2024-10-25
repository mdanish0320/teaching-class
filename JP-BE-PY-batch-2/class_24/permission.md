# Django Guardian Integration

This guide provides instructions on how to integrate the Django Guardian library for object-level permissions in your Django application.

## Prerequisites

Ensure you have Django installed and set up in your project.

## Installation

1. Install the `django-guardian` package:

   ```bash
   pip install django-guardian
   ```

## Configuration

### Update `settings.py`

1. Add `guardian` to your `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       # Other apps...
       'guardian',
   ]
   ```

2. Configure authentication backends to include Guardian:

   ```python
   AUTHENTICATION_BACKENDS = (
       'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
       'guardian.backends.ObjectPermissionBackend',  # Object-level permissions
   )
   ```

3. Set the `ANONYMOUS_USER_ID` to allow permissions for anonymous users:

   ```python
   ANONYMOUS_USER_ID = -1
   ```

## Implementing Object-Level Permissions in Views

### Update `views.py`

Create a `ProductViewSet` that utilizes Django's built-in permissions:

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

1. Run the migrations for the guardian package:

   ```bash
   python manage.py migrate
   ```

2. Create a superuser for accessing the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

## Assigning Object-Level Permissions

You can dynamically assign object-level permissions to users or groups. Below is an example of how to do this:

```python
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import User, Group

# Assign object-level permissions for a user
user = User.objects.get(username='username')  # Replace with the actual username
assign_perm('view_product', user, self)
assign_perm('change_product', user, self)
assign_perm('delete_product', user, self)

# Assign object-level permissions for a group
group = Group.objects.get(name='Product Managers')  # Replace with the actual group name
assign_perm('view_product', group, self)
assign_perm('change_product', group, self)
assign_perm('delete_product', group, self)
```

## Applying Object-Level Permissions in the Admin Interface

To apply object-level permissions in the Django admin interface, modify `admin.py` as follows:

```python
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Product

class ProductAdmin(GuardedModelAdmin):
    def has_view_permission(self, request, obj=None):
        # Check if the user has view permission at the object level
        if obj is not None:
            return request.user.has_perm('view_product', obj)
        return super().has_view_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        # Check if the user has change permission at the object level
        if obj is not None:
            return request.user.has_perm('change_product', obj)
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Check if the user has delete permission at the object level
        if obj is not None:
            return request.user.has_perm('delete_product', obj)
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        # For adding, just use the regular model-level permission
        return super().has_add_permission(request)

admin.site.register(Product, ProductAdmin)
```



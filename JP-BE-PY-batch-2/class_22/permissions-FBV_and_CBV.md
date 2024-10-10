# Permissions in Django REST Framework

In Django, permissions play a crucial role in controlling access to resources and functionalities within your application. There are generally four categories of permissions that can be implemented using Django REST Framework (DRF):

## 1. Application (Global) Level Permissions

- **Description**: These permissions apply globally across the entire application.
- **Example**: The permission `rest_framework.permissions.IsAuthenticated` is commonly used to restrict access to authenticated users only.
- **Implementation**: You can define this permission in the `settings.py` file as follows:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.IsAuthenticated',
      ],
  }
  ```

## 2. Model (Table) Level Permissions

- **Description**: These permissions are applied at the model or table level, allowing you to check whether a user has permission to perform actions (create, update, view) on specific models.
- **Example**: The permission `rest_framework.permissions.DjangoModelPermissions` is used for this purpose. To apply it to a view, you can use the `@permission_classes` decorator:
  ```python
  from rest_framework.permissions import DjangoModelPermissions
  from rest_framework.decorators import permission_classes

  @permission_classes([DjangoModelPermissions])
  class MyModelViewSet(viewsets.ModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```
- **Note**: This permission type requires a queryset to function correctly, which is only supported in Class-Based Views (CBVs). Therefore, this feature does not work automatically with Function-Based Views (FBVs).

## 3. Object Level (Row) Permissions

- **Description**: Object-level permissions are more granular and apply to individual instances of a model (or rows in a table). This allows checking if a user is permitted to view or update specific records.
- **Example**: The permission `rest_framework.permissions.DjangoObjectPermissions` can be used for this purpose.
- **Implementation**:
  ```python
  from rest_framework.permissions import DjangoObjectPermissions

  @permission_classes([DjangoObjectPermissions])
  class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```
- **Note**: Like model-level permissions, this also requires a queryset and is supported only in CBVs, meaning it won't function automatically in FBVs.

## 4. Custom Permissions

- **Description**: Custom permissions allow you to define your own permission logic based on specific requirements that may not be covered by the built-in permissions.
- **Implementation**: You can create a custom permission class by extending `BasePermission`. The `BasePermission` class has two key methods that you can override:

  1. **`has_permission(self, request, view)`**: This method is automatically called in both CBVs and FBVs. It checks whether a user has permission to perform the action at the view level.
  
  2. **`has_object_permission(self, request, view, obj)`**: This method is only automatically called in CBVs. For FBVs, you will need to invoke it manually to check permissions at the object level.

### Example of Custom Permission

Here is an example of how to implement a custom permission that checks if a user is an author or a moderator:

```python
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status

class IsAuthorOrModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user belongs to the 'moderator' group
        if request.user.groups.filter(name='moderator').exists():
            return True
        
        # Allow access only if the user is the author of the object
        return obj.author_id == request.user.id

# Usage in an API view
book = book_model.objects.get(pk=id)
if not IsAuthorOrModerator().has_object_permission(request, None, book):
    return Response({"error": "You cannot delete other authors' books"}, status=status.HTTP_403_FORBIDDEN)
```

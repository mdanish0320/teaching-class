In Django Rest Framework (DRF), the `BasePermission` class provides a way to control access to views based on user permissions. The methods `has_permission` and `has_object_permission` are two key methods used to determine if a request should be permitted.

### `has_permission` vs. `has_object_permission`

1. **`has_permission(self, request, view)`**:
   - **Purpose**: This method checks if the user has permission to access the entire view. It does not consider the specific object being accessed.
   - **Parameters**:
     - `request`: The HTTP request object.
     - `view`: The view that is being accessed.
   - **Usage**: Typically used to check permissions at a higher level, such as verifying if a user is authenticated or if they have a specific role or permission before accessing any action of the view.

2. **`has_object_permission(self, request, view, obj)`**:
   - **Purpose**: This method checks if the user has permission to perform an action on a specific object. It is called only when a specific object is being accessed.
   - **Parameters**:
     - `request`: The HTTP request object.
     - `view`: The view that is being accessed.
     - `obj`: The object that the request is trying to access.
   - **Usage**: Typically used in detail views or for actions that involve a specific instance, such as updating or deleting an object.

### Usage in Function-Based Views (FBV) and Class-Based Views (CBV)

- **Function-Based Views (FBV)**:
  - In FBV, the `has_permission` method is automatically called before the view function is executed. If it returns `False`, the view will not execute, and an appropriate HTTP response (like 403 Forbidden) will be returned.
  - The `has_object_permission` method is called within the view function when the request is related to a specific object. For instance, when using `get_object()` in the view, it will first check if the user has permission to access the view and then call `has_object_permission()` with the specific object.

- **Class-Based Views (CBV)**:
  - In CBV, DRF handles permission checks automatically. The `has_permission` method is called during the view dispatch process, before any actions (like `create`, `retrieve`, `update`, or `destroy`) are executed.
  - The `has_object_permission` method is called when the action relates to a specific instance (object), such as when retrieving a single item, updating, or deleting it. This is typically managed within the mixins that DRF provides (e.g., `RetrieveModelMixin`, `UpdateModelMixin`).

### Automatic Triggering of Methods

- **When a Request is Made**:
  - **`has_permission`**: 
    - Automatically called when a request is made to a view. If it returns `False`, the request is denied before reaching the actual view logic.
  
  - **`has_object_permission`**:
    - Automatically called only for requests that involve object-level permissions, like detail views (e.g., retrieving a single object, updating it, etc.). It is called after `has_permission` has passed.
    - If the request method (like `GET`, `PUT`, or `DELETE`) requires object-level permissions, this method is invoked with the specific object being accessed.

### Example of Usage

Here's a simple example illustrating the usage of `has_permission` and `has_object_permission` in a DRF permission class:

```python
from rest_framework.permissions import BasePermission

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

### Summary

- **`has_permission`** checks general view-level access, while **`has_object_permission`** checks access for specific objects.
- In **FBVs**, both methods are called manually within the view logic, whereas in **CBVs**, they are called automatically based on the request type.
- **`has_permission`** is called first, and if it passes, **`has_object_permission`** is called for actions involving specific objects.
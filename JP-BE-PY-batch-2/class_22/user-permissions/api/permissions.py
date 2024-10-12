from rest_framework.request import Request
from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    """
    Custom permission to allow only users in the 'author' group to create books.
    """
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='author').exists()
      
      
class IsReader(BasePermission):
    """
    Custom permission to allow only users in the 'author' group to create books.
    """
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='reader').exists()      
      
      
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

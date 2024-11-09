from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class AuthorOnlyView(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="author").exists():
            return True
        return False


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the current user is the author of the post
        return obj.author == request.user


class IsAuthorOrModerator(BasePermission):
    """
    Custom permission to allow:
    - Authors to delete their own books
    - Moderators to delete any book
    """

    def has_object_permission(self, request, view, obj):
        # Allow access if the user is a moderator
        if request.user.groups.filter(name="moderator").exists():
            return True

        # Allow access if the user is the author of the book
        return obj.author == request.user

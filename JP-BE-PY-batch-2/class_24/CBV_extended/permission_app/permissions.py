from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Custom permission to only allow superusers to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a superuser
        return request.user.is_authenticated and request.user.is_superuser

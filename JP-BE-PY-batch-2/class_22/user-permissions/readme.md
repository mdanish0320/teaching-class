```python
# create groups using admin interface
# author
# moderator
# reader

# create user
# Assuming the "reader" group already exists in your database
reader_group = Group.objects.get(name='reader')
# Create the user
user = User.objects.create(
    email="danish@gmail.com", 
    username="danish", 
    password=make_password("admin"),
    is_staff=True,            # Grants access to the admin interface
    is_superuser=True         # Grants all permissions and unrestricted access
)

# Add the user to the "reader" group
user.groups.add(reader_group)

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# views.py
from rest_framework.decorators import permission_classes, BasePermission
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny]) # allow accessing this API publically (without auth)
def get_all_books(requst: Request):
    pass


class IsAuthor(BasePermission):
    """
    Custom permission to allow only users in the 'author' group to create books.
    """
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='author').exists()

@api_view(['POST'])
@permission_classes([IsAuthor])  # Check model-level permissions
def create_book(requst: Request): # only the user having group/role 'author' can create post
    pass


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


@api_view(['DELETE']) 
@permission_classes([IsAuthorOrModerator])  # problem: permission doesn't auto trigger in FBV
def delete_book(request: Request, id):
    book = book_model.objects.get(pk=id)

    # manually trigger the method because the automatic trigger only works with queryset and queryset is a feature of CBV
    # we are using FBV
    if not IsAuthorOrModerator().has_object_permission(request, None, book):
        return Response({"error": "You cannot delete other author books"}, status=status.HTTP_403_FORBIDDEN)

    book.delete()
    return Response("successfully deleted", status=status.HTTP_200_OK)

```
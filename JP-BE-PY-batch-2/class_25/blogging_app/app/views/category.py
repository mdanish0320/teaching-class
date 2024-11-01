from rest_framework.viewsets import ModelViewSet
from ..models import Category
from ..serializers import CategorySerialzer
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..permissions import IsAuthor, IsAuthorOrModerator


# Create your views here.
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

    def get_permissions(self):
        if self.action == "list":
            # Public access to the list action
            return [AllowAny()]

        if self.action in ["update", "partial_update"]:
            # Author or Moderator can update or partially update
            return [IsAuthenticated(), IsAuthorOrModerator()]

        if self.action in ["destroy"]:
            # Only the author of the post can update, partially update, or delete
            return [IsAuthenticated(), IsAuthor()]

        # Default permission for other actions like 'retrieve'
        return [IsAuthenticated()]

from rest_framework.viewsets import ModelViewSet
from ..models import Post
from ..serializers import PostSerialzer
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..permissions import IsAuthor, IsAuthorOrModerator, AuthorOnlyView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser


# Create your views here.
class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.select_related("category").all()
    serializer_class = PostSerialzer
    parser_classes = [MultiPartParser]  # Allows file uploads

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

        if self.action == "my_posts":
            return [AuthorOnlyView()]

        # Default permission for other actions like 'retrieve'
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def my_posts(self, request):
        # Get the posts of the authenticated user
        user_posts = Post.objects.filter(author=request.user)
        serializer = self.get_serializer(user_posts, many=True)
        return Response(serializer.data)

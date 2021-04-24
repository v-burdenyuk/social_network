from django.contrib.auth import get_user_model
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import UserSerializer, PostSerializer
from posts.models.like import Like
from posts.models.post import Post
from .permissions import IsOwnerOrReadOnly, IsSelfOrReadOnly


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSelfOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    @action(detail = True, methods = ['get'])
    def like(self, request, pk=None):
        # TODO: use LikeSerializer
        post = get_object_or_404(Post.objects.all(), pk = pk)

        if Like.objects.filter(author = request.user, post = post):
            return Response(
                {"fail": f"You already liked this post '{post}'"}
            )

        Like.objects.create(author = request.user, post = post)
        return Response({"success": f"Post liked post '{post}'"})

    @action(detail = True, methods = ['get'])
    def unlike(self, request, pk=None):
        like_instance = get_object_or_404(Like.objects.all(), author = request.user, post_id = pk)
        if like_instance.delete():
            return Response({"success": f"Post unliked"})


schema_view = get_schema_view(
    openapi.Info(
        title = "Snippets API",
        default_version = 'v1',
        description = "Test description",
        terms_of_service = "https://www.google.com/policies/terms/",
        contact = openapi.Contact(email = "contact@snippets.local"),
        license = openapi.License(name = "BSD License"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

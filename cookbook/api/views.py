from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from posts.models import Post, Comment
from .permissons import IsOwnerOrReadOnly, CheckAuthor
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          CheckAuthor]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        serializer.save(author=self.request.user, post_id=post.id)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('id'))
        queryset = post.comments
        return queryset

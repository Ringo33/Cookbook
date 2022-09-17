from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from posts.models import Post, Comment
from .filters import PostFilter
from .permissons import CheckAuthor, IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnly]
    # filter_backends = [filters.SearchFilter]
    filter_backends = (DjangoFilterBackend,)
    # search_fields = ['text', ]
    filter_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        word = self.request.query_params.get('text', None)
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        if word is not None and date_from is not None and date_to is not None:
            queryset = queryset.filter(pub_date__range=(date_from, date_to)).filter(text__contains=word)
        # if word is not None:
        #     queryset = queryset.filter(text__contains=word)
        return queryset


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

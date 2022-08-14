from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CategoryListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('new/', PostCreateView.as_view(), name='add_post'),
    path('<str:category>/', CategoryListView.as_view(), name='category_post'),
    path('<str:category>/<slug:slug>/', PostDetailView.as_view(), name='detail_post'),
    path('edit/<str:category>/<slug:slug>/', PostUpdateView.as_view(), name='edit_post'),
    path('delete/<str:category>/<slug:slug>/', PostDeleteView.as_view(), name='delete_post'),
    path('add-comment/<str:category>/<slug:slug>/', CommentCreateView.as_view(), name='add_comment')
    ]

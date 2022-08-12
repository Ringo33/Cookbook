from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView
)

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('new/', PostCreateView.as_view(), name='new_post'),
    path('<str:category>/<slug:slug>/', PostDetailView.as_view(), name='detail_post'),
    ]

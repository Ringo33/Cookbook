from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PostViewSet, CommentViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/(?P<id>[0-9]+)/comments', CommentViewSet)

urlpatterns = [
     path('', include(router.urls)),
     # path('api/v1/api-token-auth/', views.obtain_auth_token)
     path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, ProfileViewSet, CommentViewSet, UserRegistrationView

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view()),
]

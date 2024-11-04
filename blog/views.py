from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .filters import PostFilter, ProfileFilter
from .permissions import IsAuthorOnly
from .serializers import PostSerializer, ProfileSerializer, CommentSerializer, UserRegistrationSerializer
from .models import Post, Profile, Comment
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (JWTAuthentication,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProfileFilter
    http_method_names = ['get', 'put', 'patch', 'delete']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsAuthorOnly()]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (JWTAuthentication, )
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsAuthorOnly()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (JWTAuthentication,)
    filter_backends = (DjangoFilterBackend, )
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsAuthorOnly()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'user': serializer.data,
            'refresh': str(RefreshToken.for_user(user)),
            'access': str(RefreshToken.for_user(user).access_token),
        })

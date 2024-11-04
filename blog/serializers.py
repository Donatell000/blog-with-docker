from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Profile, Comment


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'username', 'title', 'content', 'time_create', 'time_update')


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'email': {'required': True}, 'password': {'write_only': True}}

    @staticmethod
    def validate_email(value):
        if value is None or value == '':
            raise serializers.ValidationError("Это обязательное поле.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    @staticmethod
    def validate_username(value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Пользователь с таким никнеймом уже существует.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user

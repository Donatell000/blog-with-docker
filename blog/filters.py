import django_filters
from .models import Post, Profile


class PostFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username')

    class Meta:
        model = Post
        fields = ['title', 'username']


class ProfileFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username', label='Введите имя пользователя')
    age = django_filters.CharFilter(field_name='age', label='Введите возраст')

    class Meta:
        model = Profile
        fields = ['age']

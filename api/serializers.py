from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models.post import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'url',
            'username',
            'last_login',
            'last_activity',
        )
        read_only_fields = ('last_login', 'last_activity',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    likes_quantity = serializers.IntegerField(
        source = 'likes.count',
        read_only = True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'likes_quantity',)

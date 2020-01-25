from rest_framework import serializers

from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'created_at', 'likes',)
        read_only_fields = ('likes',)


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('user', 'post', 'post_like')

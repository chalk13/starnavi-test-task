from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import generics
from rest_framework.response import Response

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostLike(generics.UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def put(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        user = get_object_or_404(get_user_model(), username=request.user)
        try:
            Like.objects.create(user=user, post=post, post_like=True)
        except IntegrityError:
            return Response(status=200, data={'msg': 'Post already liked'})
        post.likes += 1
        post.save()
        return Response(status=201, data={'msg': 'Post liked'})


class PostUnlike(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        user = get_object_or_404(get_user_model(), username=request.user)
        try:
            obj = Like.objects.get(user=user, post=post)
            obj.delete()
            post.likes -= 1
            post.save()
        except Like.DoesNotExist:
            return Response(status=200, data={'msg': 'Post not liked'})
        return Response(status=204)

from django.urls import path

from .views import PostList, PostDetail, PostLike, PostUnlike

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/<int:pk>/like/', PostLike.as_view()),
    path('posts/<int:pk>/unlike/', PostUnlike.as_view()),
]

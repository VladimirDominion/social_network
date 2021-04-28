from django.urls import path

from posts.views import PostDetailApi, PostLikeApi, PostListApi, PostCreateApi, LikeAnalyticsApi

post_patterns = [
    path('', PostListApi.as_view(), name='post_list'),
    path('create/', PostCreateApi.as_view(), name='post_create'),
    path('analytics/', LikeAnalyticsApi.as_view(), name='post_analytics'),
    path('<int:post_id>', PostDetailApi.as_view(), name='post_detail'),
    path('<int:post_id>/like/', PostLikeApi.as_view(), name='post_like'),
]

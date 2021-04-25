from rest_framework import serializers
from rest_framework.views import APIView

from core.mixins import ApiAuthMixin
from core.pagination import get_paginated_response, LimitOffsetPagination
from posts.models import Post
from posts.selectors import post_list


class PostListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        count_likes = serializers.SerializerMethodField()

        @staticmethod
        def get_count_likes(obj):
            return getattr(obj, 'count_likes', 0)

        class Meta:
            model = Post
            fields = ('id', 'title', 'text', 'author', 'count_likes')

    class FilterSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=255, required=False)
        author_name = serializers.CharField(max_length=20, required=False)
        author_email = serializers.CharField(max_length=20, required=False)
        id = serializers.IntegerField(required=False)

    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = post_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self
        )

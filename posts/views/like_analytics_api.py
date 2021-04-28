from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from core.mixins import ApiAuthMixin
from posts.selectors import get_like_analytics


class LikeAnalyticsApi(ApiAuthMixin, APIView):
    class FilterSerializer(serializers.Serializer):
        date_from = serializers.DateField()
        date_to = serializers.DateField()

    class OutputSerializer(serializers.Serializer):
        day = serializers.DateField()
        likes = serializers.IntegerField(default=0)
        dislikes = serializers.IntegerField(default=0)

    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        date_from = filters_serializer.validated_data.get('date_from', None)
        date_to = filters_serializer.validated_data.get('date_to', None)

        analytics = get_like_analytics(date_from=date_from, date_to=date_to)
        response_data = self.OutputSerializer(list(analytics), many=True)

        return Response(response_data)

from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    PostSerializer,
)

class PostViewSet(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    @swagger_auto_schema(
        tags=['Post v1.1'],
        operation_description='',
        operation_id='sdfsdf',
        operation_summary='Test',
        security=[],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Post v1.1'],
        operation_description='',
        operation_id='Create Post',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from app.models import Post
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
)
from rest_framework import filters
from rest_framework.pagination import (
    PageNumberPagination,
    CursorPagination,
    LimitOffsetPagination,
)
from django_filters.rest_framework import DjangoFilterBackend
# from .pagination import LinkHeaderPagination, CustomPagination as CustomPagination2

from rest_framework.exceptions import (
    APIException,
    MethodNotAllowed,
    PermissionDenied,
    NotFound,
)
from drf_yasg import openapi
from app.utils.custom_exception_handler import ServiceUnavailable

class StandardPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
    # ordering = '-created_at'

class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'sid'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

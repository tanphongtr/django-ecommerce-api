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
    pagination_class = StandardPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ['title', ]  # field like
    ordering_fields = '__all__'  # order by
    # ordering = '-created_at'
    # filterset_fields = ['title', ]  # field =

    filterset_fields = {
    'title':['gte', 'lte', 'exact', 'gt', 'lt'],
}

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='List Post',
        operation_summary='Test',
        security=[],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Post'],
        operation_description='',
        operation_id='Create Post',
        operation_summary='Test',
    )
    def post(self, request, *args, **kwargs):
        # raise ServiceUnavailable
        # self.serializer_class = PostCreateSerializer
        # return super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            raise ServiceUnavailable(detail=serializer.errors)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'uuid'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        print(request.LANGUAGE_CODE)
        return super().get(request, *args, **kwargs)


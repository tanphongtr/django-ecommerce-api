from typing import Text
from django.utils.cache import get_cache_key
from drf_renderer_xlsx.mixins import XLSXFileMixin
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from app.models import Post
from .serializers import (
    PostExportSerializer,
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
from rest_framework.permissions import IsAuthenticated, BasePermission, DjangoModelPermissions as DMPer
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication
from drf_renderer_xlsx.renderers import XLSXRenderer

from app.utils.permissons import ModelPermissions, IsOwnerOrReadOnly
from rest_framework.parsers import FormParser
from rest_framework import filters
import django_filters.rest_framework
from rest_framework_simplejwt.authentication import JWTAuthentication


class StandardPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
    # ordering = '-created_at'


class PostViewSet(generics.ListCreateAPIView):
    schema = AutoSchema(
        tags=['Pets'],
        component_name='Pet',
        operation_id_base='Pet'
    )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ModelPermissions , IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication, SessionAuthentication, JWTAuthentication]
    from rest_framework.renderers import JSONRenderer, AdminRenderer, BrowsableAPIRenderer
    renderer_classes = [JSONRenderer,
                        BrowsableAPIRenderer, AdminRenderer, XLSXRenderer]
    # parser_classes = [FormParser,]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {
        'created_at': [
            'gte', 'lte', 'exact', 'gt', 'lt',
            'year__gte', 'year__lte', 'year__exact', 'year__gt', 'year__lt',
            'month__gte', 'month__lte', 'month__exact', 'month__gt', 'month__lt',
            'day__gte', 'day__lte', 'day__exact', 'day__gt', 'day__lt',
            'hour__gte', 'hour__lte', 'hour__exact', 'hour__gt', 'hour__lt',
            'minute__gte', 'minute__lte', 'minute__exact', 'minute__gt', 'minute__lt',
            'second__gte', 'second__lte', 'second__exact', 'second__gt', 'second__lt',
        ],
    }
    search_fields = ['title', 'content', 'user__username']
    ordering_fields = '__all__'

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Bearer <token>'
            ),
        ],
        tags=['Posts'],
        operation_description='',
        operation_id='List Post',
        operation_summary='',
    )

    def get(self, request, *args, **kwargs):
        from constance import config
        print(config.THEME)
        print('---', get_cache_key(request=request))

        print(request.user)
        print('========================================', request.user.id)
        # print('========================================', request.META.get('HTTP_AUTHORIZATION', b''))
        # print('========================================', request.COOKIES.get('test'))

        print("=======================", type(
            request.user.get_all_permissions()))

        from app.utils.onetime_password import OnetimePassword

        # otp = OnetimePassword().send_to_mail(mail='tanphongtr@gmail.com')

        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Bearer <token>'
            ),
        ],
        tags=['Posts'],
        operation_description='',
        operation_id='Create Post',
        operation_summary='',
    )
    def post(self, request, *args, **kwargs):
        print(request.user.id)
        print("=======================", request.user.get_all_permissions())

        return super().post(request, *args, **kwargs)


class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ModelPermissions, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    lookup_field = 'sid'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Bearer <token>'
            ),
        ],
        tags=['Posts'],
        operation_description='',
        operation_id='Get Post',
        operation_summary='',
    )
    def get(self, request, *args, **kwargs):
        print("="*10, request.user.id)
        print("="*10, request.user.get_user_permissions())

        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Bearer <token>'
            ),
        ],
        tags=['Posts'],
        operation_description='',
        operation_id='Put Post',
        operation_summary='',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Bearer <token>'
            ),
        ],
        tags=['Posts'],
        operation_description='',
        operation_id='Patch Post',
        operation_summary='',
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Bearer <token>'
            ),
        ],
        tags=['Posts'],
        operation_description='',
        operation_id='Delete Post',
        operation_summary='',
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class PostExportViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostExportSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'my_export.xlsx'

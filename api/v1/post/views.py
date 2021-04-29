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
from rest_framework.permissions import IsAuthenticated, BasePermission, DjangoModelPermissions as DMPer
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication
from drf_renderer_xlsx.renderers import XLSXRenderer

from app.utils.permissons import ModelPermissions

class StandardPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
    # ordering = '-created_at'

class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [ModelPermissions]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]
    from rest_framework.renderers import JSONRenderer, AdminRenderer, BrowsableAPIRenderer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, AdminRenderer, XLSXRenderer]
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
        operation_id='List Posffffffffft',
        operation_summary='',
    )
    def get(self, request, *args, **kwargs):
        # print(request.user)
        # print('========================================', request.user.id)
        # print('========================================', request.META.get('HTTP_AUTHORIZATION', b''))
        # print('========================================', request.COOKIES.get('test'))

        from app.utils.onetime_password import OnetimePassword

        otp = OnetimePassword().send_to_mail(mail='tanphongtr@gmail.com')

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
        print("=======================", request.user.get_all_permissions() )

        return super().post(request, *args, **kwargs)


class PostDetailViewSet(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes = [ModelPermissions]
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
        print("===============================================", request.user.id)
        print("=======================", request.user.get_user_permissions() )

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


from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

class PostExportViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'my_export.xlsx'
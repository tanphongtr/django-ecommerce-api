from rest_framework.authtoken import views
from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    Group,
    Permission,
    ContentType,
)
from .serializers import (
    UserSerializer, AuthTokenSerializer, AuthForgotPasswordSerializer
)
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, DjangoModelPermissions as DMPer



class AuthViewSet(generics.CreateAPIView):
    serializer_class = AuthTokenSerializer

    # @swagger_auto_schema(
    #     tags=['Auth'],
    #     operation_description='',
    #     operation_id='Login',
    #     operation_summary='Test',
    #     responses={
    #         # 200: AuthSerializer(),
    #     },
    # )
    def post(self, request, *args, **kwargs):
        # print(request.version)
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'user': user.username
            }
        )
    pass


class AuthLogoutViewSet(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    # @swagger_auto_schema(
    #     tags=['Auth'],
    #     operation_description='',
    #     operation_id='Login',
    #     operation_summary='Test',
    #     responses={
    #         # 200: AuthSerializer(),
    #     },
    # )
    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ):
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
    pass


class AuthForgotPasswordViewSet(generics.CreateAPIView):
    serializer_class = AuthForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        try:
            request.user.auth_token.delete()
        except (AttributeError, ):
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
    pass
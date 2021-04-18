from rest_framework.authtoken import views
from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserSignUpSerializer
from rest_framework.authtoken.models import Token


class UserSignUpViewSet(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer

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
        serializer.save()
        # user = serializer.validated_data['user']
        # token, created = Token.objects.get_or_create(user=user)
        return Response(serializer.data)
    pass
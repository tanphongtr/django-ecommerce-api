from app.serializers import Test
from rest_framework import generics, mixins, views
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer

class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserPermissionsAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response(request.user.get_all_permissions())

    Test
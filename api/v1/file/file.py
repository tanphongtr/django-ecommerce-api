from os import name
from rest_framework import generics, status
from app.models import File
from .serializers import FileSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework import permissions


class FileAPIView(generics.ListCreateAPIView):
    # authentication_classes = (BasicAuthentication, )
    # permission_classes = (permissions.IsAuthenticated, )

    queryset = File.objects.all()
    serializer_class = FileSerializer

    parser_classes = (MultiPartParser,)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class FileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'sid'
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    # def get_object(self):
    #     try:
    #         return self.filter_queryset(self.get_queryset().filter(sid=self.kwargs.get('sid')))
    #     except:
    #         raise
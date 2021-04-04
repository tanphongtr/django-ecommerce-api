from rest_framework import generics, status
from app.models import File
from .serializers import FileSerializer
from rest_framework.response import Response

class FileAPIView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

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
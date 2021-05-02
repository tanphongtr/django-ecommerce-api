from rest_framework import generics
from app.models import Json
from .serializers import JsonSerializer

class JsonAPIView(generics.ListCreateAPIView):
    queryset = Json.objects.all()
    serializer_class = JsonSerializer
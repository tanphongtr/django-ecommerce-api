from rest_framework import generics
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from .serializers import AdminLogSerializer

class AdminLogAPIView(generics.ListAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = AdminLogSerializer
    filename = 'my_export.xlsx'
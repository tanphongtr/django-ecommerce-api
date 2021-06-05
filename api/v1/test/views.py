from rest_framework import generics
from api.v1.test.serializers import AlbumSerializer, TrackSerializer
from app.models import Album, Track

class AlbumAPIView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackAPIView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
class TrackDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
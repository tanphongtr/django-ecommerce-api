from rest_framework import serializers
from app.models import Album, Track


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail',
        lookup_field='id'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'

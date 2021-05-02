from rest_framework import serializers
from app.models import Json


class JsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Json
        fields = '__all__'

from django.db.models import fields
from rest_framework import serializers
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class AdminLogSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    content_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='app_label'
    )
    

    class Meta:
        model = LogEntry
        fields = '__all__'
        depth = 1

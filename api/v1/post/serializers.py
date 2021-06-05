from django.db.models import fields
from rest_framework import serializers
from app import models
from app.models import Post

class PostSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Post.STATUS_CHOICES)
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostExportSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Post
        fields = ('title', 'content', 'user')
from rest_framework import serializers
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
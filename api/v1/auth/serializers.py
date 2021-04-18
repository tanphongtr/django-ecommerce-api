from django.conf import settings
from django.db import models
from rest_framework import serializers, exceptions
from django.contrib.auth.models import (
    User, UserManager, Group, GroupManager, Permission, PermissionManager,
)
from django.contrib.auth import authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer as _AuthTokenSerializer
from django.utils.translation import gettext_lazy as _


class AuthTokenSerializer(_AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.AuthenticationFailed(
                    msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User

from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Q


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        print(validated_data)

        # if User.objects.get(username=validated_data.get('username')):
        #     raise exceptions.AuthenticationFailed("SSS")
        user = User.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user) 
        return user
        return super().create(validated_data)


    # def validate(self, attrs):
    #     username = attrs.get('username')
    #     password = attrs.get('password')
    #     email = attrs.get('email')

    #     if username and password and email:

    #         user = User.objects.filter(Q(username=username) | Q(email=email)).exists()

    #         # The authenticate call simply returns None for is_active=False
    #         # users. (Assuming the default ModelBackend authentication
    #         # backend.)
    #         if user:
    #             msg = _('Tên người dùng hoặc email đã có người sử dụng')
    #             raise exceptions.ValidationError(
    #                 msg, code='authorization')
    #     else:
    #         msg = _('Must include "username" and "password".')
    #         raise serializers.ValidationError(msg, code='authorization')

    #     attrs['user'] = user
    #     return attrs

    def validate_username(self, value):
        """
        Check that the blog post is about Django.
        """

        user = User.objects.filter(Q(username=value)).exists()
        if user:
            msg = _('Username exist')
            raise serializers.ValidationError(msg, code='authorization')
        return value

    def validate_email(self, value):
        """
        Check that the blog post is about Django.
        """

        import re

        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            msg = _('Email is valid')
            raise serializers.ValidationError(msg, code='authorization')

        user = User.objects.filter(Q(email=value)).exists()
        if user:
            msg = _('Email exist')
            raise serializers.ValidationError(msg, code='authorization')
        return value
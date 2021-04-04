from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import (
    User, UserManager, Group, GroupManager, Permission, PermissionManager,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models=User
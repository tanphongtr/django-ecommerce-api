from django.db import models

class AppSetting(models.Model):
    name = models.CharField(max_length=255, null=False, )
    code_name = models.CharField(max_length=255, null=False, )
    value = models.

    from django.contrib.auth.models import Permission

from django.db import models
from django.core.validators import MinLengthValidator


class Organization(models.Model):
    name = models.CharField(max_length=255, null=False, )
    aliases = models.CharField( max_length=4, null=False, validators=[MinLengthValidator, ])
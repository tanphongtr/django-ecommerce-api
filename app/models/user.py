from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    

    def __str__(self):
        return super().get_username()

    def delete(self, using, keep_parents):
        """Overide detele()"""
        self.is_active = False
        return super().save()
    pass
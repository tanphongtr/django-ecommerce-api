from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self) -> str:
        return self.get_full_name()
    # Override
    def delete(self, using, keep_parents):
        self.is_active = False
        return super().save()
    pass
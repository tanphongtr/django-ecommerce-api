from django.db import models
import uuid
from app.models import User
# from django.contrib.auth.models import User

class Post(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, )
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'posts'

    #Override
    def delete(self, using=None, keep_parents=False):
        self.title='deleted 003'
        return super().save()

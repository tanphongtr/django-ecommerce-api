from django.db import models
import uuid
# from app.models import User
from django.contrib.auth.models import User

class Post(models.Model):
    sid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,)
    content = models.TextField(max_length=1000, blank=True, default='', )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, )
    update_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'posts'

    #Override
    # def delete(self, using=None, keep_parents=False):
    #     self.title='deleted 003'
    #     return super().save()

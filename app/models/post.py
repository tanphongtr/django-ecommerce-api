from django.db import models
import uuid
# from app.models import User
from django.contrib.auth.models import User
from tinymce.models import HTMLField

PENDING = 0
DONE = 1

class Post(models.Model):
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DONE, 'Done'),
    )
    sid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,)
    content = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, )
    status = models.BooleanField(choices=STATUS_CHOICES, default=PENDING, )
    update_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'posts'

    #Override
    # def delete(self, using=None, keep_parents=False):
    #     self.title='deleted 003'
    #     return super().save()

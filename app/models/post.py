from django.db import models
import uuid

class Post(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,)


    class Meta:
        db_table = 'posts'

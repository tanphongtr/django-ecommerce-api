from django.db import models
import uuid

class Post(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'posts'

    #Override
    def delete(self, using=None, keep_parents=False):
        self.title='deleted 003'
        return super().save()

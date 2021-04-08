import os
import uuid
from django.db import models


class FileField(models.FileField):
    def generate_filename(self, instance, filename):
        _, ext = os.path.splitext(filename)
        filename = f'{uuid.uuid4().hex}{ext}'
        return super().generate_filename(instance, filename)


class File(models.Model):
    sid = models.UUIDField(default=uuid.uuid4, unique=True, null=False)
    file_url = FileField(upload_to='files/%Y/%m/%d', )
    created_at = models.DateTimeField(auto_now=True, null=False, )

    class Meta:
        db_table = 'files'

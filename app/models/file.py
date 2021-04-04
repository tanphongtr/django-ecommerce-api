import uuid
from django.db import models
from django.core.validators import FileExtensionValidator

class FileField(models.FileField):
    
    def generate_filename(self, instance, filename):
        print(filename)
        import os

        from hashlib import sha256

        _, ext = os.path.splitext(filename) 
        print(ext)
        filename = f'{uuid.uuid4().hex}{ext}'
        return super().generate_filename(instance, filename)

class File(models.Model):
    sid = models.UUIDField(default=uuid.uuid4, unique=True, null=False)
    file_url = FileField(
        upload_to='files/%Y/%m/%d',
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )

    import os
    def filename(self):
        return os.path.basename(self.file.file_url)
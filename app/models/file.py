import uuid
from django.db import models
from app.models import FileField
from django.utils.translation import ugettext_lazy as _


class File(models.Model):
    sid = models.UUIDField(default=uuid.uuid4, unique=True, null=False)
    file_url = FileField(upload_to='files/%Y/%m/%d', )
    created_at = models.DateTimeField(auto_now=True, null=False, )

    class Meta:
        db_table = 'files'
        verbose_name = _("File")
        verbose_name_plural = _("Files")

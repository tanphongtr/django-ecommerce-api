from django.db import models

class Json(models.Model):

    data = models.TextField()
    data2 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True, null=False)
    class Meta:
        db_table = 'jsons'
from rest_framework import serializers
from app.models import File
from rest_framework.exceptions import ErrorDetail, ValidationError, NotFound
from .exceptions import ServiceUnavailable
from django.core.validators import FileExtensionValidator
from django.conf import settings
import os
from django.utils.translation import gettext_lazy as _

class FileField(serializers.FileField):
    def to_representation(self, value):
        print(self.context)
        return super().to_representation(value)
class FileSerializer(serializers.ModelSerializer):
    file_url = FileField(write_only=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )
    test = serializers.SerializerMethodField()

    class Meta:
        model = File
        # fields = "__all__"
        exclude = ('id', )

    

    def get_test(self, obj):
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri('/download/' + str(obj.sid))
        return _("Phongtran")

    def is_valid(self, raise_exception=False):
        try:
            return super().is_valid(raise_exception=raise_exception)
        except ServiceUnavailable as ex:
            raise ex

    # def save(self, **kwargs):
    #     try:
    #         return super().save(**kwargs)
    #     except:
    #         raise NotFound("SDfsdfds")
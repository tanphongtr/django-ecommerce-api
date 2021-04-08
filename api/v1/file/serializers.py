from rest_framework import serializers
from app.models import File
from .exceptions import ServiceUnavailable
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class FileField(serializers.FileField):
    def to_representation(self, value):
        return super().to_representation(value)

class FilesSerializer(serializers.Serializer):
    test = serializers.CharField()
    pass
class FileSerializer(serializers.ModelSerializer):
    sid = serializers.UUIDField(read_only=True, )
    file_url = FileField(
        required=True,
        write_only=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg'], )
        ]
    )
    url = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    # test = FilesSerializer()

    class Meta:
        model = File
        # fields = ('sid', 'url', 'file_url', 'created_at', )
        # fields = "__all__"
        exclude = ('id', )

    # Custom Field
    def get_url(self, obj):
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri('/download/' + str(obj.sid))
        return _("Phongtran")

    def is_valid(self, raise_exception=False):
        try:
            return super().is_valid(raise_exception=raise_exception)
        except ServiceUnavailable as ex:
            raise ex

    def validate(self, attrs):
        if attrs.get('file_url', None):
            attrs.get('file_url', None).size
        return super().validate(attrs)
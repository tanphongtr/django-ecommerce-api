from rest_framework import serializers
from rest_framework.exceptions import ErrorDetail, ValidationError
from app.models import File
from .exceptions import ServiceUnavailable
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class FilesSerializer(serializers.Serializer):
    test = serializers.CharField()
    pass


class FileSerializer(serializers.ModelSerializer):
    sid = serializers.UUIDField(read_only=True, )
    # file_url = serializers.FileField(
    #     required=True,
    #     write_only=True,
    #     validators=[
    #         FileExtensionValidator(allowed_extensions=['jpg'], )
    #     ]
    # )
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

        # try:
        #     return super().is_valid(raise_exception=raise_exception)
        # except ServiceUnavailable as ex:
        #     raise ex

        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            # print(self.errors)
            raise ServiceUnavailable(self.errors)

        return not bool(self._errors)

    def validate(self, attrs):
        if attrs.get('file_url', None):
            attrs.get('file_url', None).size
        return super().validate(attrs)

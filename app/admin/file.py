from django.contrib import admin
from app.models import File
from django.utils.html import format_html
from django.urls import path
from django_api.views import file_downloading


class FileAdmin(admin.ModelAdmin):

    list_display = ('sid', 'download', 'created_at', )
    search_fields = ['sid']
    filter=['sid']
    list_filter=['sid']

    def download(self, obj):
        # return format_html(f'<a target="_blank" href="/download/{obj.sid}">Download</a>', obj.sid)
        return path('download/<uuid:test/', file_downloading)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    pass


admin.site.register(File, FileAdmin)

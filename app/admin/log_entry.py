from django.contrib import admin
from django.contrib.admin.models import LogEntry


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'change_message', )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # readonly_fields = ('content_type', 'user', 'action_time')
    pass


admin.site.register(LogEntry, LogEntryAdmin)

from django.contrib import admin
from app.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', )


admin.site.register(Employee, EmployeeAdmin)

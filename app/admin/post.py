from django.contrib import admin
from django import forms
from import_export.forms import ImportForm, ConfirmImportForm
from import_export.widgets import ForeignKeyWidget
from app.models import Post
from django.contrib.auth.models import User
from import_export import resources, fields, widgets
from import_export.admin import ExportActionMixin, ImportExportModelAdmin, ImportExportActionModelAdmin, ImportMixin

class CustomImportForm(ImportForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True)
class CustomConfirmImportForm(ConfirmImportForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True)


class PostResource(resources.ModelResource):
    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(User, 'username'))


    class Meta:
        model = Post

class PostAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = PostResource
    list_display = ('sid', 'title', 'status')

    # def get_import_form(self):
    #     return CustomImportForm

    # def get_confirm_import_form(self):
    #     return CustomConfirmImportForm


admin.site.register(Post, PostAdmin)

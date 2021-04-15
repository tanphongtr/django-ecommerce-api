from django.contrib import admin
from app.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('sid', 'title', )


admin.site.register(Post, PostAdmin)

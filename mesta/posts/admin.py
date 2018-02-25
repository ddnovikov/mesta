from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)

from django.contrib import admin
from attachments.models import Image, File


class ImageAdmin(admin.ModelAdmin):
    class Meta:
        model = Image


class FileAdmin(admin.ModelAdmin):
    class Meta:
        model = File


admin.site.register(Image, ImageAdmin)
admin.site.register(File, FileAdmin)
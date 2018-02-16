from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


def file_upload_location(instance, filename):
    return f'files/{instance.id}_{filename}'


class File(models.Model):
    file = models.FileField(upload_to=file_upload_location)

    name = models.CharField(max_length=200, verbose_name='Название', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        db_table = "files"
        verbose_name = "Файл"
        verbose_name_plural = "Изображения"

    def __repr__(self):
        return f'File(title={self.name})'

    def __str__(self):
        return self.name

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


def upload_location_image(instance, filename):
    return f'images/{instance.id}_{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=upload_location_image,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    name = models.CharField(max_length=200, verbose_name='Название', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        db_table = "images"
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __repr__(self):
        return f'Image(title={self.name})'

    def __str__(self):
        return self.name

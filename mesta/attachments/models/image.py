from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


def image_upload_location(instance, filename):
    return f'images/{instance.id}_{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=image_upload_location,
                              height_field='height_field',
                              width_field='width_field',
                              blank=True,
                              null=True,
                              verbose_name='Изображение')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    # Image or image url should be filled while creating Image object.
    # image_url = models.URLField(blank=True,
    # verbose_name='Ссылка на изображение')

    name = models.CharField(max_length=200,
                            blank=True,
                            verbose_name='Название')
    description = models.TextField(blank=True,
                                   verbose_name='Описание')

    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
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

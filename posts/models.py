from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from shared_tools.slugs import create_slug
from places.models import Place
from attachments.models import Image, File


def upload_location(instance, filename):
    return f'{instance.id}/{filename}'


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название поста')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    content = models.TextField(blank=True, null=True, verbose_name='Текст поста')
    tags = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Теги')

    main_image = models.ImageField(upload_to=upload_location,
                                   null=True,
                                   blank=True,
                                   height_field='height_field',
                                   width_field='width_field',
                                   verbose_name='Главное изображение поста')
    height_field = models.IntegerField(default=0, blank=True, verbose_name='Высота изображения в пикселях')
    width_field = models.IntegerField(default=0, blank=True, verbose_name='Ширина изображения в пикселях')

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Автор поста')

    place = models.ForeignKey(Place, blank=True, null=True, on_delete=models.SET_NULL)

    draft = models.BooleanField(default=False, verbose_name='Черновик / Видимость объекта')

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Время последнего изменения')

    images = GenericRelation(Image, verbose_name='Прикреплённые изображения')
    files = GenericRelation(File, verbose_name='Прикреплённые файлы')

    class Meta:
        ordering = ["-timestamp", "-updated"]
        db_table = "posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __repr__(self):
        return f'Post(title={self.title}, timestamp={self.timestamp})'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})


@receiver(pre_save, sender=Post)
def pre_save_post_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, 'title')

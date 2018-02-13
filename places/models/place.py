from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from phonenumber_field.modelfields import PhoneNumberField

from attachments.models import Image, File
from shared_tools.slugs import create_slug


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(blank=True, unique=True, verbose_name='Slug')
    description = models.TextField(blank=True, verbose_name='Описание')
    draft = models.BooleanField(default=False, verbose_name='Черновик / Видимость объекта')
    rating = models.FloatField(blank=True, null=True, verbose_name='Рейтинг')
    tags = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Теги')

    country = models.CharField(max_length=40, blank=True, verbose_name='Страна')
    region = models.CharField(max_length=200, blank=True, verbose_name='Регион')
    city = models.CharField(max_length=200, blank=True, verbose_name='Город')
    zip_code = models.CharField(max_length=10, blank=True, verbose_name='Почтовый индекс')
    street = models.CharField(max_length=200, blank=True, verbose_name='Улица')
    building_number = models.CharField(max_length=20, blank=True, verbose_name='Номер здания')

    latitude = models.FloatField(blank=True, null=True, verbose_name='Широта')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Долгота')

    subway = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Ближайшие станции метро')
    site = models.URLField(blank=True, verbose_name='Сайт')
    telephone = PhoneNumberField(blank=True, verbose_name='Телефон')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              verbose_name='Пользователь-владелец или представитель места')

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Время последнего изменения')

    images = GenericRelation(Image, verbose_name='Прикреплённые изображения')
    files = GenericRelation(File, verbose_name='Прикреплённые файлы')

    class Meta:
        db_table = "places"
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __repr__(self):
        return f'Place(name={self.name})'

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Place)
def pre_save_place_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, 'name')
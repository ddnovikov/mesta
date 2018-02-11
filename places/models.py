from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from attachments.models import Image, File


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    description = models.TextField(blank=True, verbose_name='Описание')
    draft = models.BooleanField(default=False, verbose_name='Черновик / Видимость объекта')
    rating = models.FloatField(blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name='Рейтинг')
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


def upload_location_menu(instance, filename):
    return f'menus/{instance.id}_{filename}'


class FoodService(Place):
    place_type = models.IntegerField(choices=[(1, "Ресторан"),
                                              (2, "Кафе"),
                                              (3, "Кофейня"),
                                              (4, "Фаст-фуд"),
                                              (5, "Бар")])
    menu = models.FileField(upload_to=upload_location_menu)
    parking = models.NullBooleanField(verbose_name='Парковка')
    bank_cards = models.NullBooleanField(verbose_name='Приём банковских карт')
    wi_fi = models.NullBooleanField(verbose_name='Вай-фай')
    banquets = models.NullBooleanField(verbose_name='Банкеты')
    delivery = models.NullBooleanField(verbose_name='Доставка')
    catering = models.NullBooleanField(verbose_name='Кейтеринг')

    class Meta:
        db_table = "foodservices"
        verbose_name = "Заведение общественного питания"
        verbose_name_plural = "Заведения общественного питания"

    def __repr__(self):
        return f'FoodService(name={self.name}, type_={self.place_type})'

    def __str__(self):
        return self.name

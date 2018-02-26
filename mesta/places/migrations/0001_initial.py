# Generated by Django 2.0.2 on 2018-02-25 08:50

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import mesta.places.models.food_service
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('short_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Короткое описание')),
                ('long_description', models.TextField(blank=True, verbose_name='Длинное описание')),
                ('draft', models.BooleanField(default=True, verbose_name='Черновик / Видимость объекта')),
                ('rating', models.FloatField(blank=True, null=True, verbose_name='Рейтинг')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None, verbose_name='Теги')),
                ('country', models.CharField(max_length=40, verbose_name='Страна')),
                ('region', models.CharField(max_length=200, verbose_name='Регион')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='Почтовый индекс')),
                ('street', models.CharField(blank=True, max_length=200, verbose_name='Улица')),
                ('building_number', models.CharField(blank=True, max_length=20, verbose_name='Номер здания')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('subway', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None, verbose_name='Ближайшие станции метро')),
                ('site', models.URLField(blank=True, verbose_name='Сайт')),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Телефон')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'db_table': 'places',
            },
        ),
        migrations.CreateModel(
            name='FoodService',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.Place')),
                ('place_type', models.IntegerField(blank=True, choices=[(1, 'Ресторан'), (2, 'Кафе'), (3, 'Кофейня'), (4, 'Фаст-фуд'), (5, 'Бар'), (6, 'Винотека'), (7, 'Пекарня'), (8, 'Кондитерская'), (9, 'Гастропаб'), (10, 'Чайная')], null=True, verbose_name='Тип заведения')),
                ('menu', models.FileField(blank=True, null=True, upload_to=mesta.places.models.food_service.upload_location_menu, verbose_name='Меню')),
                ('parking', models.NullBooleanField(verbose_name='Парковка')),
                ('bank_cards', models.NullBooleanField(verbose_name='Приём банковских карт')),
                ('wi_fi', models.NullBooleanField(verbose_name='Вай-фай')),
                ('banquets', models.NullBooleanField(verbose_name='Банкеты')),
                ('delivery', models.NullBooleanField(verbose_name='Доставка')),
                ('catering', models.NullBooleanField(verbose_name='Кейтеринг')),
            ],
            options={
                'verbose_name': 'Заведение общественного питания',
                'verbose_name_plural': 'Заведения общественного питания',
                'db_table': 'foodservices',
            },
            bases=('places.place',),
        ),
        migrations.AddField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь-владелец или представитель места'),
        ),
    ]
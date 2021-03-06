# Generated by Django 2.0.2 on 2018-02-25 08:50

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import mesta.posts.models.post


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название поста')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Текст поста')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None, verbose_name='Теги')),
                ('main_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=mesta.posts.models.post.post_upload_location, verbose_name='Главное изображение поста', width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0, verbose_name='Высота изображения в пикселях')),
                ('width_field', models.IntegerField(blank=True, default=0, verbose_name='Ширина изображения в пикселях')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик / Видимость объекта')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'posts',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]

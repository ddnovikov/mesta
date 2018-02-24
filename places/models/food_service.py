from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from shared_tools.misc.slugs import create_slug
from .place import Place


def upload_location_menu(instance, filename):
    return f'menus/{instance.id}_{filename}'


class FoodService(Place):
    place_type = models.IntegerField(choices=[(1, "Ресторан"),
                                              (2, "Кафе"),
                                              (3, "Кофейня"),
                                              (4, "Фаст-фуд"),
                                              (5, "Бар")],
                                     blank=True,
                                     null=True,
                                     verbose_name='Тип заведения')
    menu = models.FileField(upload_to=upload_location_menu, blank=True, null=True, verbose_name='Меню')
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
        return f'FoodService(name={self.name}, place_type={self.place_type})'

    def __str__(self):
        return self.name

    @property
    def about_service(self):
        res = []
        service_props = [
            'place_type',
            'parking',
            'bank_cards',
            'wi_fi',
            'banquets',
            'delivery',
            'catering',
        ]

        bools = {True: 'Да', False: 'Нет', None: 'Неизвестно'}

        for p in service_props:
            cur_attr = getattr(self, p)

            if cur_attr is not None:
                if isinstance(cur_attr, bool):
                    res.append((self._meta.get_field(p).verbose_name, bools[cur_attr]))
                else:
                    res.append((self._meta.get_field(p).verbose_name, cur_attr))

        res.append(('Теги', self.tags_as_string))

        return res

    @property
    def layout_info(self):
        return [(('about', 'О ресторане'), self.about_service),
                (('contacts', 'Контактная информация'), self.contacts)]


@receiver(pre_save, sender=FoodService)
def pre_save_place_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, 'name')

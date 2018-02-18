from django import template
from django.forms import fields

from shared_tools.misc.slugs import create_slug

register = template.Library()


@register.filter(name='field_type')
def field_type(field):
    field_name = field.field

    if isinstance(field_name, fields.CharField) or isinstance(field_name, fields.FloatField):
        return 'std'

    elif isinstance(field_name, fields.NullBooleanField):
        return 'null-bool'


@register.filter(name='slugify')
def slugify(html_name, arg):
    return f'{create_slug(html_name)}-{arg}'
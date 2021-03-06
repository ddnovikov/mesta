from django import template
from django.forms import fields, models, widgets

from ..tools.slugs import create_slug

register = template.Library()


@register.filter(name='field_type')
def field_type(field):
    field_t = field.field

    if isinstance(field_t, fields.CharField) or \
       isinstance(field_t, fields.FloatField):

        if not isinstance(field_t.widget, widgets.Textarea):
            return 'std'
        else:
            return 'txt'

    elif isinstance(field_t, fields.NullBooleanField):
        return 'null-bool'

    elif isinstance(field_t, fields.TypedChoiceField) or \
         isinstance(field_t, models.ModelChoiceField):

        return 'typed-choice'


@register.filter(name='slugify_field')
def slugify_field(html_name, arg):
    return f'{create_slug(html_name)}-{arg}'

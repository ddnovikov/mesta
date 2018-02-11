import unidecode

from django.utils.text import slugify


def create_slug(instance, slug_src_field, new_slug=None, slug_field_name='slug'):
    if new_slug is None:
        slug = slugify(unidecode.unidecode(getattr(instance, slug_src_field)))
    else:
        slug = new_slug

    filter_query = {slug_field_name: slug}
    same_slug_elem = instance.__class__.objects.filter(**filter_query).first()

    if same_slug_elem:
        new_slug = f'{slug}-{same_slug_elem.id}'
        return create_slug(instance, slug_src_field, new_slug=new_slug, slug_field_name=slug_field_name)

    return slug

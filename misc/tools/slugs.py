import unidecode

from django.utils.text import slugify


def create_slug(input_,
                slug_src_field=None,
                new_slug=None,
                slug_field_name='slug',
                uniqueness_check=True):

    if slug_src_field is not None:
        if new_slug is None:
            slug = slugify(unidecode.unidecode(getattr(input_, slug_src_field)))
            if not uniqueness_check:
                return slug
        else:
            slug = new_slug

    else:
        if new_slug is None:
            slug = slugify(unidecode.unidecode(input_))
            return slug

    filter_query = {slug_field_name: slug}
    same_slug_elem = input_.__class__.objects.filter(**filter_query).first()

    if same_slug_elem:
        new_slug = f'{slug}-{same_slug_elem.id}'
        return create_slug(input_, slug_src_field, new_slug=new_slug, slug_field_name=slug_field_name)

    return slug

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from places.models import Place, FoodService
from places.forms import PlaceForm, FoodServiceForm
from attachments.models import Image
from attachments.forms import ImageForm


def places_home(request):
    all_services = FoodService.objects.all()
    search_query = request.GET.get('q')

    context = {
        'all_services': all_services,
        'search_query': search_query,
    }

    return render(request, 'home.html', context)


@login_required
def place_create(request, place_base_type='place'):
    forms_dict = {
        'place': PlaceForm,
        'food-service': FoodServiceForm,
    }

    Form = forms_dict.get(place_base_type)
    if Form is None:
        return Http404('Page not found.')

    form = Form(request.POST or None)
    image_form = ImageForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            place_instance = form.save(commit=False)
            place_instance.owner = request.user
            place_instance.save()

        if image_form.is_valid() and request.FILES:
            image = image_form['image']
            image_instance = Image(image=image, content_object=place_instance)
            image_instance.save()

        messages.success(request, 'Место успешно создано.')
        return redirect(place_instance)

    context = {
        'place_form': form,
        'image_form': image_form,
        'null_bool_values': {1: ['Неизвестно', None], 2: ['Да', True], 3: ['Нет', False]},
        'title': 'Создать место',
        'submit_value': 'Создать место',
    }

    return render(request, 'place_form.html', context)


@login_required
def place_update(request, slug=None):
    instance = FoodService.objects.get(slug=slug)

    if isinstance(instance, FoodService):
        form = FoodServiceForm(request.POST or None, instance=instance)
    else:
        instance = get_object_or_404(Place, slug=slug)
        form = PlaceForm(request.POST or None, instance=instance)

    image_form = ImageForm(request.POST or None, request.FILES or None, instance=instance.images.all().first())

    if request.method == 'POST':
        if form.is_valid():
            place_instance = form.save(commit=False)
            place_instance.owner = request.user
            place_instance.save()

        if image_form.is_valid() and request.FILES:
            image = image_form['image']
            image_instance = Image(image=image, content_object=place_instance)
            image_instance.save()

        messages.success(request, 'Место успешно создано.')
        return redirect(place_instance)

    context = {
        'place_form': form,
        'image_form': image_form,
        'null_bool_values': {1: ['Неизвестно', None], 2: ['Да', True], 3: ['Нет', False]},
        'title': f'Изменить место {instance.name}',
        'submit_value': 'Сохранить изменения',
    }

    return render(request, 'place_form.html', context)


def place_detail(request, slug=None):
    instance = get_object_or_404(Place, slug=slug)
    image = instance.images.all().first()

    context = {
        'instance': instance,
        'image': image,
    }

    return render(request, 'place_detail.html', context)


def place_list(request):
    all_fss = FoodService.objects.all()

    context = {
        'all_fss': all_fss,
        'title': 'Все заведения'
    }

    return render(request, 'place_list.html', context)


# def place_delete(request):
#     pass
#
# ImageFormSet = generic_inlineformset_factory(Image, form=ImageForm, min_num=0)
# image_formset = ImageFormSet(request.POST or None, request.FILES or None)

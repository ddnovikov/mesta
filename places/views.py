from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from attachments.models import Image
from attachments.forms import ImageForm
from places.models import Place, FoodService
from places.forms import PlaceForm, FoodServiceForm
from places.documents import FoodServiceDocument
from shared_tools.misc.chain_search import chain_search


def places_home(request):
    all_services = FoodService.objects.all()
    carousel = []

    for i in [63, 61, 64]:
        instance = FoodService.objects.filter(pk=i).first()
        image = instance.images.all().first()

        if image is not None:
            image = image.image
            carousel.append((instance, image))

    context = {
        'all_services': all_services,
        'carousel': carousel,
        'carousel_amount': range(len(carousel)),
        'tags': ['Рестораны',
                 'Крафт-бары',
                 'Азиатская кухня',
                 'Кофейни',
                 'Японская кухня',
                 'Итальянская кухня',
                 'Русская кухня'],
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
            image = image_form.cleaned_data['image']
            try:
                image_instance = Image(image=image, content_object=place_instance)
            except ObjectDoesNotExist:
                return HttpResponse('Неверный запрос. Нельзя сохранить изображение, '
                                    'не связав его с объектом.', status=500)
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
def place_update(request, slug):
    instance = FoodService.objects.get_or_none(slug=slug)

    if instance is not None:
        form = FoodServiceForm(request.POST or None, instance=instance)
    else:
        instance = get_object_or_404(Place, slug=slug)
        form = PlaceForm(request.POST or None, instance=instance)

    image_form = ImageForm(request.POST or None,
                           request.FILES or None,
                           instance=instance.images.all().first())

    if request.method == 'POST':
        if form.is_valid():
            place_instance = form.save(commit=False)
            place_instance.owner = request.user
            place_instance.save()

        if image_form.is_valid() and request.FILES:
            image = image_form.cleaned_data['image']
            instance.images.all().delete()
            try:
                image_instance = Image(image=image, content_object=place_instance)
            except ObjectDoesNotExist:
                return HttpResponse('Неверный запрос. Нельзя сохранить изображение, '
                                    'не связав его с объектом.', status=500)
            image_instance.save()

        messages.success(request, 'Место успешно создано.')
        return redirect(place_instance)

    context = {
        'place_form': form,
        'image_form': image_form,
        'null_bool_values': {1: ['Неизвестно', None], 2: ['Да', True], 3: ['Нет', False]},
        'title': f'Изменить место "{instance.name}"',
        'submit_value': 'Сохранить изменения',
    }

    return render(request, 'place_form.html', context)


def place_detail(request, slug):
    instance = FoodService.objects.get_or_none(slug=slug)
    if instance is None:
        instance = get_object_or_404(Place, slug=slug)

    context = {
        'instance': instance,
    }

    return render(request, 'place_detail.html', context)


def place_list(request):
    all_fss = FoodService.objects.all()

    context = {
        'place_objects': all_fss,
        'title': 'Каталог заведений'
    }

    return render(request, 'place_list.html', context)


def place_tag(request):
    query = request.GET.get('tag', '').strip()

    if query:
        places_by_tag = FoodService.objects.filter(tags__icontains=query)
    else:
        return HttpResponse('Задан пустой фильтр по тегам.')

    context = {
        'all_fss': places_by_tag,
        'title': f'Каталог заведений с тегом "{query}"',
    }

    return render(request, 'place_list.html', context)


def place_search(request):
    search_query = request.GET.get('q')

    if search_query:
        search_results = chain_search({'name': search_query}, FoodServiceDocument.search())
        search_results = search_results.to_queryset()
    else:
        return HttpResponse('Задан пустой поисковый запрос.')

    context = {
        'place_objects': search_results,
        'title': f'Результаты поиска по запросу "{search_query}"',
    }

    return render(request, 'place_list.html', context=context)



def place_delete(request, slug):
    instance = FoodService.objects.get_or_none(slug=slug)
    if instance is None:
        instance = get_object_or_404(Place, slug=slug)

    instance.delete()
    messages.success(request, 'Объект успешно удалён.')

    return redirect('places:home')

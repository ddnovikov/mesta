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

    if request.method == 'POST':
        form = Form(request.POST or None)

        if place_base_type == 'place':
            if form.is_valid():
                place_instance = form.save(commit=False)
                place_instance.owner = request.user
                place_instance.save()

                messages.success(request, 'Место успешно создано.')
                return redirect(place_instance)

        elif place_base_type == 'food-service':
            image_form = ImageForm(request.POST or None, request.FILES or None)

            if form.is_valid() and image_form.is_valid():
                place_instance = form.save(commit=False)
                place_instance.owner = request.user
                place_instance.save()

                image = image_form['image']
                image_instance = Image(image=image, content_object=place_instance)
                image_instance.save()

                messages.success(request, 'Место успешно создано.')
                return redirect(place_instance)

    else:
        form = Form(request.POST or None)
        image_form = ImageForm(request.POST or None, request.FILES or None)

    context = {
        'place_form': form,
        'null_bool_values': ['Да', 'Нет', 'Неизвестно'],
        'title': 'Создать место',
        'submit_value': 'Создать место',
    }

    return render(request, 'place_form.html', context)


def place_detail(request, slug=None):
    instance = get_object_or_404(Place, slug=slug)
    images = instance.images.all()

    context = {
        'instance': instance,
        'images': images,
    }

    return render(request, 'place_detail.html', context)


def place_list(request):
    all_fss = FoodService.objects.all()

    context = {
        'all_fss': all_fss,
    }

    return render(request, 'place_list.html', context)


# def place_delete(request):
#     pass
#
# ImageFormSet = generic_inlineformset_factory(Image, form=ImageForm, min_num=0)
# image_formset = ImageFormSet(request.POST or None, request.FILES or None)

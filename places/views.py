from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404

from places.models import Place, FoodService
from places.forms import PlaceForm


def places_home(request):
    all_services = FoodService.objects.all()
    search_query = request.GET.get('q')

    context = {
        'all_services': all_services,
        'search_query': search_query,
    }

    return render(request, 'home.html', context)


def place_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PlaceForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        messages.success(request, 'Место успешно создано.')
        return redirect(instance)

    context = {
        'place_form': form,
        'title': 'Создать место',
        'submit_value': 'Создать место',
    }

    return render(request, 'place_form.html', context)


def place_detail(request, slug=None):
    instance = get_object_or_404(Place, slug=slug)

    context = {
        'instance': instance,
    }

    return render(request, 'place_detail.html', context)



# def place_update(request):
#     pass
#
#
# def place_delete(request):
#     pass
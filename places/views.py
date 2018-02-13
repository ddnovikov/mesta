from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from places.models import FoodService
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
        instance.user = request.user
        instance.save()
        messages.success(request, 'Место успешно создано.')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'place_form': form,
        'title': 'Создать место',
        'submit_value': 'Создать место',
    }

    return render(request, 'place_form.html', context)


# def place_detail(request):
#     pass
#
#
# def place_update(request):
#     pass
#
#
# def place_delete(request):
#     pass
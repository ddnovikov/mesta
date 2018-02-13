from django.shortcuts import render

from places.models import FoodService


def places_home(request):
    all_services = FoodService.objects.all()
    search_query = request.GET.get('q')

    context = {
        'all_services': all_services,
        'search_query': search_query,
    }

    return render(request, 'home.html', context)


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
from django.contrib import admin

from .models import Place, FoodService


class PlaceAdmin(admin.ModelAdmin):
    class Meta:
        model = Place

    list_display = ['name', 'country', 'city', 'owner', 'updated']
    list_filter = ['updated', 'owner', 'country', 'city']
    search_fields = ['name', 'long_description', 'country', 'city']


class FoodServiceAdmin(PlaceAdmin):
    class Meta:
        model = FoodService


admin.site.register(Place, PlaceAdmin)
admin.site.register(FoodService, FoodServiceAdmin)
from django import forms

from places.models import Place


class PlaceForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    class Meta:
        model = Place
        fields = [
            'name',
            'slug',
            'description',
            'draft',
            'tags',
            'country',
            'region',
            'city',
            'zip_code',
            'street',
            'building_number',
            'latitude',
            'longitude',
            'subway',
            'site',
            'telephone',
        ]

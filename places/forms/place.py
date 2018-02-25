from django import forms

from ..models import Place


class PlaceForm(forms.ModelForm):
    short_description = forms.CharField(label='Короткое описание', required=False, widget=forms.Textarea)
    long_description = forms.CharField(label='Длинное описание', required=False, widget=forms.Textarea)

    class Meta:
        model = Place
        fields = [
            'name',
            'slug',
            'short_description',
            'long_description',
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

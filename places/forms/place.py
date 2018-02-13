from django import forms

from places.models import Place


class PlaceForm(forms.ModelForm):
    # content = forms.CharField(widget=PagedownWidget(show_preview=False))
    # publish = forms.DateField(widget=forms.SelectDateWidget)
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

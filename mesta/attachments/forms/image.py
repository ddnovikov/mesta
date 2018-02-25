from django import forms

from ..models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField(required=False,
                             label='Изображение')

    class Meta:
        model = Image
        fields = [
            'image'
        ]

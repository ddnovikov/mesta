from django import forms

from attachments.models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Image
        fields = [
            'image'
        ]

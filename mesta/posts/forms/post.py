from django import forms

from ..models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(label='Текст поста',
                              required=False,
                              widget=forms.Textarea)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags',
            'place',
        ]

from django import forms
from .models import Post, Faq, Image


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category')


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('title', 'image', 'credits')


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields = ('question', 'answer','is_visible')

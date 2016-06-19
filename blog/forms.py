from django import forms
from .models import Post, Faq


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields = ('question', 'answer','is_visible')

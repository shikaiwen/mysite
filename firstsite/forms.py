
from django.contrib import admin
from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    title = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    class Meta:
        model = Post
        fields = ('__all__')


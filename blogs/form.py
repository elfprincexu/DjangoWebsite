from django.forms import ModelForm
from django import forms
from .models import Blog
from pagedown.widgets import AdminPagedownWidget


# create blog form
class BlogForm(ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget(show_preview=False))


    class Meta:
        model = Blog
        fields = ['title', 'author', 'content', 'coverimg', ]

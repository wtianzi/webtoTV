from django import forms
from django.forms import ModelForm
from .models import WebURL, WordUnknown

class WebURLForm(ModelForm):
    class Meta:
        model = WebURL
        fields = '__all__'

class WordUnknownForm(ModelForm):
    class Meta:
        model = WordUnknown
        fields = '__all__'

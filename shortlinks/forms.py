from django import forms
from .models import *


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ("long_url",)
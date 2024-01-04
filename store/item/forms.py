from django import forms
from .models import Item


class Item(forms.Form):
    class Meta:
        model = Item
        # fields = []

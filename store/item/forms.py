from django import forms
from .models import Item


class create_item_form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["category", "item_name", "price", "stock", "description", "image"]

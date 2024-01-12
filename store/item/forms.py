from django import forms
from .models import Item


class create_item_form(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(create_item_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Item
        fields = ["category", "item_name", "price", "stock", "description"]

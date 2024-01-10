from django import forms
from .models import Item


class create_item_form(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.user = kwargs.get("user")
            kwargs.pop("user")

    class Meta:
        model = Item
        fields = ["category", "item_name", "price", "stock", "description"]

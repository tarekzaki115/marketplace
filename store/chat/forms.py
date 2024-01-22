from django import forms
from .models import Message


class chat_form(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["body"]

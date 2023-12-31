from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class register_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class change_user_form(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

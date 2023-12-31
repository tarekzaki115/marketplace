from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import customUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_seller = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    object = customUserManager()

    def __str__(self):
        return self.email

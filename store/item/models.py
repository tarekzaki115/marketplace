from django.db import models
from user.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="+", blank=True, null=True
    )

    def __str__(self):
        return self.category_name


class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=0,
        related_name="seller",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, null=False
    )
    item_name = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    sold = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    image = models.URLField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.item_name

from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="+", blank=True, null=True
    )

    def __str__(self):
        return self.category_name


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, null=False
    )
    item_name = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    sold = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.item_name

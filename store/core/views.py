from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from item.models import Category, Item


class indexView(generic.ListView):
    model = Item
    template_name = "core\index.html"

    def get_queryset(self):
        self.items = Item.objects.all().order_by("created_at")[:2]
        return self.items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.items
        return context

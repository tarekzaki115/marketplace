from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Count

from item.models import Category, Item


class indexView(generic.ListView):
    model = Item
    template_name = "core\index.html"

    def get_queryset(self):
        self.catagories = Category.objects.filter(category__isnull=True).order_by(
            "category_name"
        )[:3]
        self.items = Item.objects.all().order_by("created_at")[:2]
        return self

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.items
        context["catagories"] = self.catagories
        return context


class itemDetailView(generic.DetailView):
    model = Item
    template_name = "core\item.html"

    def get_object(self):
        self.item = Item.objects.get(pk=self.kwargs["pk"])
        return self

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = self.item
        return context

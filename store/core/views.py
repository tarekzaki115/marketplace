from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic, View
from django.db.models import Count
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages


from item.models import Category, Item
from user.models import User
from user.forms import UserCreationForm, UserChangeForm


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


class userCreateView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "core/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("register")
        else:
            messages.error(request, "Registration was not successful")
            return redirect("register")


class userChangeView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

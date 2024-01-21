from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from django.db.models import Count
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from item.models import Category, Item
from user.models import User
from chat.models import Message
from user.forms import register_user_form, change_user_form
from item.forms import create_item_form, edit_item_form


class indexView(generic.ListView):
    model = Item
    template_name = "core/index.html"

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
    template_name = "core/item.html"

    def get_object(self):
        self.item = Item.objects.get(pk=self.kwargs["pk"])
        return self

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = self.item
        return context


class userCreateView(View):
    def get(self, request):
        form = register_user_form()
        return render(request, "core/register.html", {"form": form})

    def post(self, request):
        form = register_user_form(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("index")
        else:
            messages.error(request, "Registration was not successful")
            return redirect("register")


class userEditView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "editUser"

    def get(self, request):
        form = change_user_form(instance=request.user)
        return render(request, "core/editUser.html", {"edit_form": form})

    def post(self, request):
        form = change_user_form(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Edit is successful")
            return redirect("index")
        else:
            messages.error(request, "Edit is unsuccessful")
            return redirect("editUser")


class changeUserPasswordView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "changeUserPassword"

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, "core/changeUserPassword.html", {"form": form})

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "You successfully changed your password")
            return redirect("index")
        else:
            messages.error(request, "Password is invalid")
            return redirect("changeUserPassword")


class loginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "core/login.html", {"login_form": form})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
                return redirect("login")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")


class logoutView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "logout"

    def get(self, request):
        logout(request)
        messages.success(request, "You are Logged out")
        return redirect("index")


class addItemView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_seller:
            form = create_item_form()
            return render(request, "core/createItem.html", {"form": form})
        else:
            messages.error(request, "Please apply for the seller program")
            return redirect("index")

    def post(self, request):
        form = create_item_form(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, "You added a new Item successfully")
            return redirect("createItem")
        else:
            messages.error(request, "Adding Item failed")
            return redirect("createItem")


class dashboardView(LoginRequiredMixin, View):
    def get(self, request):
        items = Item.objects.filter(user=request.user)
        for item in items:
            print(item.pk)
        return render(request, "core/dashboard.html", {"items": items})


class editItemView(UpdateView):
    model = Item
    fields = ["category", "item_name", "price", "stock", "description", "image"]
    template_name = "core/editItem.html"
    success_url = reverse_lazy("dashboard")


class deleteItemView(DeleteView):
    model = Item
    success_url = reverse_lazy("dashboard")
    template_name = "core/deleteItem.html"


class SearchItemView(View):
    def get(self, request, pk=None, search=None):
        if pk and search == None:
            category = Category.objects.get(pk=pk)
            items = Item.objects.filter(category=category)
            context = {"category": category, "items": items}
            return render(request, "core/search.html", context)
        elif pk and search:
            query = self.request.GET.get("q")
            category = Category.objects.get(pk=pk)
            items = Item.objects.filter(
                Q(item_name__contains=query) & Q(category=category)
            )
            context = {"category": category, "items": items}
            return render(request, "core/search.html", context)

        elif pk == None and search:
            query = self.request.GET.get("q")
            items = Item.objects.filter(item_name__contains=query)
            context = {"items": items}
            return render(request, "core/search.html", context)
        else:
            categories = Category.objects.all()
            items = Item.objects.all()
            context = {"categories": categories, "items": items}
            return render(request, "core/search.html", context)


"sender = part1 and recev = part2  OR sender = part2 and recev = part1"


class chatView(View):
    def get(self, request, sender_pk, receiver_pk):
        messages = Message.get_messages(sender_pk, receiver_pk)
        return render(request, "core/chat.html", {"messages": messages})

    def post(self, request, sender_pk, receiver_pk):
        return

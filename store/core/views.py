from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


class indexView(generic.ListView):
    template_name = "core\index.html"

    def get_queryset(self):
        return

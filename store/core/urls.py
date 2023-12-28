from django.urls import path
from .views import *

urlpatterns = [
    path("", indexView.as_view(), name="index"),
    path("<int:pk>/", itemDetailView.as_view(), name="item"),
]

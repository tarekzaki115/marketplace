from django.urls import path
from .views import *


urlpatterns = [
    path("", indexView.as_view(), name="index"),
    path("<int:pk>/", itemDetailView.as_view(), name="item"),
    path("register/", userCreateView.as_view(), name="register"),
    path("editUser/", userEditView.as_view(), name="editUser"),
    path("editPass/", changeUserPasswordView.as_view(), name="changeUserPassword"),
    path("login/", loginView.as_view(), name="login"),
    path("logout/", logoutView.as_view(), name="logout"),
    path("createItem/", addItemView.as_view(), name="createItem"),
    path("dashboard/", dashboardView.as_view(), name="dashboard"),
    path("editItem/<int:pk>/", editItemView.as_view(), name="editItem"),
    path("deleteItem/<int:pk>/", deleteItemView.as_view(), name="deleteItem"),
]

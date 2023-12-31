from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import register_user_form, change_user_form


class CustomUserAdmin(UserAdmin):
    add_form = register_user_form
    form = change_user_form
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_active",
        "first_name",
        "last_name",
        "is_seller",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
        "is_seller",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_seller",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)

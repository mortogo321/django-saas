from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdminConfig(UserAdmin):
    model = User
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    list_filter = [
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    search_fields = [
        "email",
        "first_name",
        "last_name",
    ]
    ordering = ["-created_at"]
    fieldsets = [
        (
            None,
            {"fields": ["email"]},
        ),
        (
            "Personal",
            {
                "fields": [
                    "first_name",
                    "last_name",
                ]
            },
        ),
        (
            "Permissions",
            {
                "fields": [
                    "is_staff",
                    "is_supervisor",
                    "is_active",
                ]
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ],
            },
        ),
    ]


admin.site.register(User, UserAdminConfig)

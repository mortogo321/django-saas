from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Profile, User


class UserProfile(admin.StackedInline):
    model = Profile


class UserAdminConfig(UserAdmin):
    model = User
    list_display = [
        "email",
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
    ]
    ordering = ["-created_at"]
    fieldsets = [
        (
            None,
            {"fields": ["email"]},
        ),
        (
            "Permissions",
            {
                "fields": [
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ]
            },
        ),
    ]
    inlines = [UserProfile]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ],
            },
        ),
    ]


admin.site.register(User, UserAdminConfig)

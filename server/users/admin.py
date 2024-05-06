from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Profile, User


class UserAdminConfig(UserAdmin):
    model = User
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("-created_at",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_supervisor",
                    "is_active",
                )
            },
        ),
        (
            "Personal",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Profile)

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(
        User,
        auto_now=True,
    )

    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=255,
        blank=True,
    )
    address1 = models.CharField(
        max_length=255,
        blank=True,
    )
    address2 = models.CharField(
        max_length=255,
        blank=True,
    )
    city = models.CharField(
        max_length=255,
        blank=True,
    )
    state = models.CharField(
        max_length=255,
        blank=True,
    )
    zipcode = models.CharField(
        max_length=255,
        blank=True,
    )
    country = models.CharField(
        max_length=255,
        blank=True,
    )

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name

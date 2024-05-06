from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not username:
            raise ValueError(_("Username is required."))

        if not email:
            raise ValueError(_("Email address is required."))

        email = self.normalize_email(email.lower())
        user = self.model(
            username=username,
            email=email,
            **kwargs,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        user = self.create_user(
            username,
            email,
            password=password,
            **kwargs,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

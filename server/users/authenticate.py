from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest


class ModelBackend(ModelBackend):
    def authenticate(
        self,
        request: HttpRequest,
        username=None,
        password=None,
        **kwargs,
    ) -> AbstractBaseUser | None:
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

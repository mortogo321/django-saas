from django.urls import path, re_path

from .views import (
    LogoutView,
    UserProviderAuthView,
    UserTokenObtainPairView,
    UserTokenRefreshView,
    UserTokenVerifyView,
)

urlpatterns = [
    re_path(
        r"^o(?P<provider>\S+)/$/", UserProviderAuthView.as_view(), name="provider-auth"
    ),
    path("jwt/create", UserTokenObtainPairView.as_view()),
    path("jwt/refresh", UserTokenRefreshView.as_view()),
    path("jwt/verify", UserTokenVerifyView.as_view()),
    path("logout", LogoutView.as_view()),
]

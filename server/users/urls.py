from django.urls import path

from .views import (
    LogoutView,
    UserTokenObtainPairView,
    UserTokenRefreshView,
    UserTokenVerifyView,
)

urlpatterns = [
    path("jwt/create/", UserTokenObtainPairView.as_view()),
    path("jwt/refresh/", UserTokenRefreshView.as_view()),
    path("jwt/verify/", UserTokenVerifyView.as_view()),
    path("logout/", LogoutView.as_view()),
]

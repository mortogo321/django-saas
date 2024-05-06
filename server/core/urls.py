from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("users.urls")),
    path("order/", include("order.urls")),
    path("payment/", include("payment.urls")),
]

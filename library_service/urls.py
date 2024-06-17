from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/borrowing/", include("borrowing.urls", namespace="borrowing")),
    path("api/library/", include("library.urls", namespace="library")),
    path("api/payment/", include("payment.urls", namespace="payment")),
    path("api/user/", include("user.urls", namespace="user")),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

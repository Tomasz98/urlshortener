from django.urls import path
from .views import CreateShortURL, RedirectToOriginalView

urlpatterns = [
    path("create/", CreateShortURL.as_view(), name="create"),
    path(
        "shrt/<short_code>/",
        RedirectToOriginalView.as_view(),
        name="redirect_to_original",
    ),
]

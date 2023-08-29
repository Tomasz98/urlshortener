from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from rest_framework import generics, status
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer


class CreateShortURL(generics.CreateAPIView):
    """
    API endpoint to create a shortened URL.

    This view handles the creation of a shortened URL. When provided with a valid original URL,
    it returns a unique shortened URL path in the format `http://localhost:8000/api/shrt/<short_code>/`.

    Attributes:
        queryset: Default queryset, fetching all URL objects.
        serializer_class: Serializer used to validate and save the original URL, generate a unique short_code.

    Methods:
        create: Method overrides the default `CreateAPIView` method to customize the response format.
    """

    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            response_data = {
                "shortened_url": request.build_absolute_uri(
                    f"/api/shrt/{response.data['short_code']}/"
                )
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return response


class RedirectToOriginalView(View):
    """
    View responsible for redirecting a short URL to original URL.

    When accessed with a valid short code, this view make a redirection to the original URL.
    If the short code doesn't exist, it returns a 404 error.

    Methods:
        get: Handles the GET request by fetching the URL object using the provided short_code
             and redirecting to the original URL.
    """

    def get(self, request, *args, **kwargs):
        short_code = kwargs.get("short_code")
        url_obj = get_object_or_404(URL, short_code=short_code)
        return redirect(url_obj.original_url)

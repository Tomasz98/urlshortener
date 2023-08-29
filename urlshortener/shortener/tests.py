from django.test import TestCase
from django.urls import reverse
from .models import URL


class URLShortenerTests(TestCase):
    def test_create_short_url(self):
        """Test if a short URL is created successfully."""
        url = reverse("create")
        response = self.client.post(url, {"original_url": "https://google.com"})

        self.assertEqual(response.status_code, 201)
        self.assertIn("shortened_url", response.data)

        # Extract short_code from the shortened_url
        short_code = response.data["shortened_url"].split("/")[-2]
        self.assertTrue(response.data["shortened_url"].endswith(short_code + "/"))

    def test_redirect_to_original_url(self):
        """Test if the redirection using a short URL works correctly."""
        original_url = "https://google.com"
        url_obj = URL.objects.create(original_url=original_url)

        url = reverse("redirect_to_original", kwargs={"short_code": url_obj.short_code})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, original_url)

    def test_non_existent_short_url(self):
        """Test if a non-existent short URL returns a 404 error."""
        non_existent_code = "123456"
        url = reverse("redirect_to_original", kwargs={"short_code": non_existent_code})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

from django.db import models
import string
import random


def generate_unique_code():
    """
        Generate a unique short code for URL shortening.

        The function creates a random combination of uppercase, lowercase, and digits
        until it produces a unique code not already present in the database.

        Returns:
            str: A unique short code of specified length (default is 14 characters).
        """
    length = 14
    while True:
        code = "".join(
            random.choices(
                string.ascii_uppercase + string.ascii_lowercase + string.digits,
                k=length,
            )
        )
        if not URL.objects.filter(short_code=code).exists():
            break
    return code


class URL(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.URLField()
    short_code = models.CharField(
        max_length=15, unique=True, default=generate_unique_code
    )
    created_at = models.DateTimeField(auto_now_add=True)

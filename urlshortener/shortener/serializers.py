from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    """
    Serializer for the URL model.

    This serializer represents the URL model with its original URL and the associated unique short code.

    Attributes:
        model: The associated model to which this serializer is tied, in this case, the URL model.
        fields: Tuple containing the fields of the model to be serialized or deserialized.
                Includes 'original_url' and 'short_code'.
    """

    class Meta:
        model = URL
        fields = ("original_url", "short_code")

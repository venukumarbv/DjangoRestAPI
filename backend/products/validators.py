from rest_framework import serializers

from .models import Product


# def validate_<filed_name>(self, value):
def validate_title(self, value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} Product already exists")
    return value
from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


def validate_price(value):
    if Product.objects.filter(price__exact=value).exists():
        raise serializers.ValidationError(f"This price is already price:{value} in database...")
    return value


unique_price_validator = UniqueValidator(queryset=Product.objects.all())

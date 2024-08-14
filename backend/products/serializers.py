from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import (
    Product,
    ProductComment,
    ProductProperty,
    ProductRating
)
from .validations import validate_price, unique_price_validator


class ProductRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRating
        exclude = ['id']


class ProductCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductComment
        exclude = ['id']


class ProductPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductProperty
        exclude = ['id']


class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField(method_name='get_discount_price', read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(view_name="product_detail", lookup_field="pk", default="")
    price = serializers.CharField(validators=[validate_price, unique_price_validator])
    comments = serializers.SerializerMethodField(method_name='get_comments', read_only=True)

    def get_comments(self, obj):
        instance = ProductComment.objects.filter(product=obj.id).order_by('-id')[:5]
        # print('product_prefetch', product_prefetch)
        # instance = Product.comments_set.filter.all().order_by('-id')[:3]
        return ProductCommentSerializer(instance, context=self.context, many=True).data

    def validate_title(self, value):
        if Product.objects.filter(title__exact=value).exists():
            raise serializers.ValidationError(f"This title already title:{value} in database...")
        return value

    def get_discount_price(self, obj):
        return round(float(obj.price) * 0.8, 2)

    def get_detail_url(self, obj):
        return reverse("product_detail", kwargs={"pk": obj.pk}, request=self.context.get('request'))

    class Meta:
        model = Product
        exclude = ['id']

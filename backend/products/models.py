import uuid
from django.db.models import (
    Model,
    UUIDField,
    CharField,
    DecimalField,
    TextField,
    ForeignKey,
    DateTimeField,
    CASCADE,
    DO_NOTHING,
    OneToOneField,
    IntegerField,
    SmallIntegerField
)
from django.db.models.functions import Now
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductBase(Model):

    uu_id = UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Product(ProductBase):

    name = CharField(max_length=120)
    content = TextField(blank=True, null=True)
    title = CharField(max_length=120)
    price = DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def __str__(self):
        return f"Product {self.title} <product:{self.uu_id}>"

    @property
    def sale_price(self):
        return round(float(self.price) * 0.8, 2)

    class Meta:
        db_table = 'product'
        ordering = ["title"]
        verbose_name_plural = "Products"


class ProductRating(ProductBase):

    user = ForeignKey(User, on_delete=DO_NOTHING, related_name="users")
    product = ForeignKey(Product, on_delete=CASCADE, related_name='ratings')
    rating = SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.product} <rating{self.uu_id}>"


class ProductComment(ProductBase):

    product = ForeignKey(Product, on_delete=CASCADE, related_name='comments')
    comment = TextField()
    created_at = DateTimeField(db_default=Now())

    def __str__(self):
        return f"{self.product} <comment:{self.uu_id}>"

    class Meta:
        db_table = 'product_comment'
        verbose_name_plural = "ProductComments"


class ProductProperty(ProductBase):

    product = OneToOneField(Product, on_delete=CASCADE, null=True)
    width = IntegerField(default=15)
    length = IntegerField(default=15)
    manufacturer = TextField(blank=False, null=True)

    def __str__(self):
        return f"{self.product} property <product:{self.uu_id}>"

    class Meta:
        db_table = 'product_property'
        verbose_name_plural = "ProductProperties"

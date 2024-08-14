from django.contrib import admin
from .models import Product, ProductComment, ProductProperty


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    pass

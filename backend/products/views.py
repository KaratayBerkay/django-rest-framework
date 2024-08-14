from django.urls import path
from django.shortcuts import render
from django.db.models import Prefetch
from .views_collection.product import (
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView
)
from .views_collection.product_comment import (
    ProductCommentDetailView,
    ProductCommentCreateView,
    ProductCommentUpdateView,
    ProductCommentDeleteView,
    ProductCommentListView
)
from .views_collection.product_rating import (
    ProductRatingCreateView,
    ProductRatingListView,
    ProductRatingDeleteView,
    ProductRatingDetailView,
    ProductRatingUpdateView
)


def test_product(request):
    from .models import Product, ProductComment
    comments_prefetch = Prefetch(
        lookup="comments",
        queryset=ProductComment.objects.filter(
            comment__istartswith="a",
        )
    )
    products = Product.objects.prefetch_related(comments_prefetch)
    return render(request=request, template_name='product_comments.html', context={"products": products})


def test_with_pre_product(request):
    from .models import ProductComment, Product
    ProductComment.objects.prefetch_related(None)
    Product.objects.prefetch_related(None)
    comments = ProductComment.objects.all()
    products = Product.objects.all()
    return render(request=request, template_name='product_comments.html', context={"products": products})


def test_product_ratings(request):
    from .models import ProductRating
    ratings = ProductRating.objects.only("product__title", "product__content", "rating").select_related('product')
    return render(request=request, template_name='product_ratings.html', context={"ratings": ratings})


def test_product_with_ratings(request):
    from .models import ProductRating
    ratings = ProductRating.objects.only("product__title", "rating").all()
    return render(request=request, template_name='product_ratings.html', context={"ratings": ratings})


# Product Endpoint Views
product_detail_view = ProductDetailView.as_view()
product_create_view = ProductCreateView.as_view()
product_update_view = ProductUpdateView.as_view()
product_delete_view = ProductDeleteView.as_view()
product_list_view = ProductListView.as_view()

# Product Endpoint Views
product_url_patterns = [
    path("product/<int:pk>", product_detail_view, name="product_detail"),
    path("product/<int:pk>/update", product_update_view, name="product_update"),
    path("product/<int:pk>/delete", product_delete_view, name="product_delete"),
    path("product/create", product_create_view, name="product_create"),
    path("product/list", product_list_view, name="product_list"),
]

product_comment_detail_view = ProductCommentDetailView.as_view()
product_comment_create_view = ProductCommentCreateView.as_view()
product_comment_update_view = ProductCommentUpdateView.as_view()
product_comment_delete_view = ProductCommentDeleteView.as_view()
product_comment_list_view = ProductCommentListView.as_view()

# Product Comment Endpoint Views
product_comment_url_patterns = [
    path("comment/<int:pk>", product_comment_detail_view, name="product_comment_detail"),
    path("comment/<int:pk>/update", product_comment_update_view, name="product_comment_update"),
    path("comment/<int:pk>/delete", product_comment_delete_view, name="product_comment_delete"),
    path("comment/create", product_comment_create_view, name="product_comment_create"),
    path("comment/list", product_comment_list_view, name="product_comment_list"),
]


product_rating_detail_view = ProductRatingDetailView.as_view()
product_rating_update_view = ProductRatingUpdateView.as_view()
product_rating_create_view = ProductRatingCreateView.as_view()
product_rating_delete_view = ProductRatingDeleteView.as_view()
product_rating_list_view = ProductRatingListView.as_view()


# Product Rating Endpoint Views
product_rating_url_patterns = [
    path("rating/<int:pk>", product_rating_detail_view, name="product_rating_detail"),
    path("rating/<int:pk>/update", product_rating_update_view, name="product_rating_update"),
    path("rating/<int:pk>/delete", product_rating_delete_view, name="product_rating_delete"),
    path("rating/create", product_rating_create_view, name="product_rating_create"),
    path("rating/list", product_rating_list_view, name="product_rating_list"),
]

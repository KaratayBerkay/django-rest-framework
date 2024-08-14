from . import views

from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = ([
    path("test", views.test_product),
    path("testwopre", views.test_with_pre_product),
    path("testratings", views.test_product_ratings),
    path("testratingswosel", views.test_product_with_ratings),
    path("auth", obtain_auth_token),
    *views.product_url_patterns, *views.product_comment_url_patterns, *views.product_rating_url_patterns
]) + debug_toolbar_urls()

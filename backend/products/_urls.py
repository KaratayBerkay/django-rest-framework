from . import views_collection
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = ([
    path("list", views_collection.product_view),
    path("create", views_collection.product_create)
])
urlpatterns = format_suffix_patterns(urlpatterns)


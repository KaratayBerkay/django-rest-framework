from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("user/list", views.UserListView.as_view(), name="user-list"),
    path("auth", obtain_auth_token),
    path("", views.api_home),
]

from django.urls import path
from .views import (
    home_views, Foundform, register_views, login_views,
    logout_views, search_items, all_items, services_view, about_view
)

urlpatterns = [
    path("", home_views, name="home"),
    path("foundform/", Foundform, name="foundform"),
    path("items/", all_items, name="items"),
    path("search/", search_items, name="search"),
    path("services/", services_view, name="services"),
    path("about/", about_view, name="about"),
    path("register/", register_views, name="register"),
    path("login/", login_views, name="login"),
    path("logout/", logout_views, name="logout"),
]
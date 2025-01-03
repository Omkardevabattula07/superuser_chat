from django.urls import path
from . import views

urlpatterns = [
    path("",views.base_art,name="base_art"),
    path("register_art/",views.register_art,name="register_art"),
    path("login_art/",views.login_art,name="login_art")
]

from django.urls import path
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path("signup/", signup_view),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]

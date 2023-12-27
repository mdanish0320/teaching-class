from django.urls import path
from . import views


urlpatterns = [
    path("register", views.RegisterUser.as_view()),
    path("admin/register", views.RegisterAdmin.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getData),
    path("get_db", views.get_db),
]
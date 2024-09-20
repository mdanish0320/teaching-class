from django.urls import path
from . import views

urlpatterns = [
    path("persons/", views.getData),
]
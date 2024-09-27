from django.urls import path
from . import views

urlpatterns = [
    path("persons/", views.query_params_example),
    path('persons/<int:id>/', views.path_params_example)
]
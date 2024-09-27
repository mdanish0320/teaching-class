from django.urls import path
from .views import get_categories_or_create_category, get_or_update_or_delete_category

urlpatterns = [
    path("categories/", get_categories_or_create_category),
    path("categories/<int:id>", get_or_update_or_delete_category)
]

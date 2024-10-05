from django.urls import path
from .views import get_categories_or_create_category, get_or_update_or_delete_category, create_or_get_products
from .views import create_or_get_categories_2, create_or_get_products_2

urlpatterns = [
    path("categories/", get_categories_or_create_category),
    path("categories/<int:id>", get_or_update_or_delete_category),

    path("categories_2/", create_or_get_categories_2),
    path("products_2/", create_or_get_products_2),
]

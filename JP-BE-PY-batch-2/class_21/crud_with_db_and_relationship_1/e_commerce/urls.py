from django.urls import path
from .views_category import get_categories_or_create_category, get_or_update_or_delete_category
from .views_product import get_products_or_create_products, get_or_update_or_delete_product, reverse_category
from . import views_product_without_relation

urlpatterns = [
    path("categories/", get_categories_or_create_category),
    path("categories/<int:id>", get_or_update_or_delete_category),

    path("products/", get_products_or_create_products),
    path("products/reverse_category", reverse_category),
    path("products/<int:id>", get_or_update_or_delete_product),

    path("products_old/", views_product_without_relation.get_products_or_create_products)
]


from django.urls import path
from .views import product, categories

urlpatterns = [
    path("products/", product.create_or_get_customers),
    path("products/assign/", product.assign_categories),

    
    path("categories/", categories.create_or_get_categories),
]

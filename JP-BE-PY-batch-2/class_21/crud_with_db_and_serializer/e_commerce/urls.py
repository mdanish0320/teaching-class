from django.urls import path
from . import views_with_serializer 
from . import views_without_serializer 

urlpatterns = [
    path("categories/", views_without_serializer.get_categories_or_create_category),
    path("categories/<int:id>", views_without_serializer.get_or_update_or_delete_category)
]

urlpatterns += [
    path("categories_2/", views_with_serializer.get_categories_or_create_category),
    path("categories_2/<int:id>", views_with_serializer.get_or_update_or_delete_category)
]


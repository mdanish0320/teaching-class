from django.urls import path
from .views import CategoryCreateListAPIView, CategoryRetriveUpdateDestroy

urlpatterns = [
    path("categories/", CategoryCreateListAPIView.as_view()),
    path("categories/<int:pk>", CategoryRetriveUpdateDestroy.as_view()),
]

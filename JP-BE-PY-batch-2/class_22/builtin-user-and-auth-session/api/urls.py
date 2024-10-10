from django.urls import path
from .views import create_or_get_users, create_or_get_posts, login_view, logout_view

urlpatterns = [
    path("users/", create_or_get_users),
    path("posts/", create_or_get_posts),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

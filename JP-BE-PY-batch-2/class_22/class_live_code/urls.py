from django.urls import path

from .views import signup_view, login_view, logout_view, profile_view
from .views_jwt import login_view as login_view_2,  profile_view as profile_view_2
from .views_custom_user import login_view as login_view_3,  profile_view as profile_view_3, logout_view as logout_view_3, signup_view as signup_view_3
from .views_permission import login_view as login_view_4,  profile_view as profile_view_4, logout_view as logout_view_4, signup_view as signup_view_4

urlpatterns = [
    path('users/signup', signup_view),
    path('users/login', login_view),
    path('users/logout', logout_view),
    path('users/profile', profile_view),


    
    path('users_2/login', login_view_2),
    path('users_2/profile', profile_view_2),
    # path('users_2/logout', login_view_2),


    path('users_3/signup', signup_view_3),
    path('users_3/login', login_view_3),
    path('users_3/logout', logout_view_3),
    path('users_3/profile', profile_view_3),


    path('users_4/signup', signup_view_4),
    path('users_4/login', login_view_4),
    path('users_4/logout', logout_view_4),
    path('users_4/profile', profile_view_4),
]

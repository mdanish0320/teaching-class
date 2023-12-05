from django.urls import path
from . import views

urlpatterns = [
    # static data
    path('static/person/list', views.get_static_persons),
    
    # data from db
    path('dynamic/person/list', views.get_dynamic_persons),
    path('dynamic/person/add', views.add_dynamic_persons),
    path('dynamic/person/update/<id>', views.update_dynamic_persons),
    path('dynamic/person/delete/<id>', views.update_delete_persons),
]
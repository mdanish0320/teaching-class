from django.urls import path
from . views import PersonAPIView_1, PersonAPIView_2
urlpatterns = [
    path("person_apiview", PersonAPIView_1.as_view()),
    path("person_apiview/<id>", PersonAPIView_2.as_view())
]
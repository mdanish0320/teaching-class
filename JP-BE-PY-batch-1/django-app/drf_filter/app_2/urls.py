from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import PersonConcrete_Create_And_List, PersonConcrete_Read_Update_AND_Delete, PersonMixin_Create_And_List, PersonMixin_Read_Update_AND_Delete, PersonGenerics_1, PersonGenerics_2


urlpatterns = [
    # Generics Concrete
    path("concrete", PersonConcrete_Create_And_List.as_view()),
    path("concrete/<id>", PersonConcrete_Read_Update_AND_Delete.as_view()),

    # Generics Mixin
    path("person_gen_mixin", PersonMixin_Create_And_List.as_view()),
    path("person_gen_mixin/<id>", PersonMixin_Read_Update_AND_Delete.as_view()),

    # GenericsAPIView
    path("person_gen", PersonGenerics_1.as_view()),
    path("person_gen/<id>", PersonGenerics_2.as_view()),

]
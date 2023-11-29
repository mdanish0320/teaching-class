# Setup
## install django globally
pip install django

## use django CLI tool django-admin to create project
django-admin startproject myproject

## create requirements.txt
create "requirements.txt" file inside your project "myproject"
write module name "djangorestframework"

## install requitements
pip install -r requirements.txt

# Create GET API with in-memory data

## open settings.py and enter your new installed module 'rest_framework' in INSTALLED_APPS
create new folder "api" beside "manage.py" and create two files inside it. urls.py and views.py
create a GET API

## views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {"name": "danish", "email": "danish@gmail.com"}
    return Response(person)


## urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getData),
]


## update myproject/urls.py
add api/urls using include

## run command
python manage.py runserver



# Fetch Data from database instead of in-memory

## create a new app inside myproject
python manage.py startapp base

## resgister this new app inside myproject
update settings.py and add 'base' inside INSTALLED_APPS

## create model
update base/models and add code

class Item(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

## create migration file
python manage.py makemigrations

## run migration 
python manage.py migrate

## add data into db using shell
python manage.py shell

from base.models import Item
Item(name="Item 1")

## run server
python manage.py runserver


# Django App Setup and Server Instructions

## Setup

1. **Install Django Globally**  
   `pip install django`

2. **Create a New Django Project**  
   Use the Django CLI tool `django-admin` to create a new project:  
   `django-admin startproject main`

3. **Rename Project**
   Rename outer folder `main` to `myproject_2`

4. **Create requirements.txt**  
   Inside your project directory (`myproject_2`), create a file named `requirements.txt` and add the following line to specify the Django REST framework:  
   `djangorestframework`

5. **Install Requirements**  
   Install the packages listed in `requirements.txt`:  
   `pip install -r requirements.txt`

6. **Create a GET API with In-Memory Data**

   - **Update settings.py**  
     Open `main/settings.py` and add `'rest_framework'` to the `INSTALLED_APPS` list:  
     ```python
     INSTALLED_APPS = [
         ...
         'rest_framework',
     ]
     ```

   - **Create an API Directory**  
     Create a new folder named `api` beside `manage.py`. Inside the `api` folder, create two files: `urls.py` and `views.py`.

   - **Define the GET API in views.py**  
     Open `api/views.py` and add the following code:  
     ```python
     from rest_framework.response import Response
     from rest_framework.decorators import api_view

     @api_view(['GET'])
     def getData(request):
         person = [{"name": "danish", "email": "danish@gmail.com"}]
         return Response(person)
     ```

   - **Set Up URLs in urls.py**  
     Open `api/urls.py` and add the following code:  
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path("users/", views.getData),
     ]
     ```

   - **Update Project URLs**  
     Open `main/urls.py` and include the api URLs:  
     ```python
     from django.urls import path, include

     urlpatterns = [
         path('api/', include('api.urls')),
         ...
     ]
     ```

7. **Run the Development Server**  
   Go inside the project `myproject_2` (where you can see the file `manage.py`) and then run the following command to start the Django development server:  
   `python manage.py runserver`

You can now access your GET API at [http://127.0.0.1:8000/api/users/](http://127.0.0.1:8000/api/users/).

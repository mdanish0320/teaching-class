# Django App Setup and Server Instructions

## Setup

1. **Install Django Globally**  
   `pip install django`

2. **Create a New Django Project**  
   Use the Django CLI tool `django-admin` to create a new project:  
   `django-admin startproject main`

3. **Rename Project**
   Rename outer folder `main` to `myproject_3`

4. **Create requirements.txt**  
   Inside your project directory (`myproject_3`), create a file named `requirements.txt` and add the following line to specify the Django REST framework:  
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
        

      @api_view(['GET', 'POST'])
      def create_and_get_all_users(request):
          if request.method == 'GET':
              print("fetching all users")
              
              # Access query parameters
              param1 = request.query_params.get('param1')  # Example: /api/persons/?param1=value
              param2 = request.query_params.get('param2')  # Example: /api/persons/?param2=value
              print(param1, param2)

              person = [{"name": "danish", "email": "danish@gmail.com"}]
              return Response(person)
          elif request.method == 'POST':
              print("creating new user")

              # Access JSON input
              data = request.data  # Data will contain parsed JSON
              value1 = data.get('key1')
              value2 = data.get('key2')
              print(value1, value2)

              person = [{"name": "danish", "email": "danish@gmail.com"}, {"name": "fahad", "email": "fahad@gmail.com"}]
              return Response(person)

      @api_view(['GET', 'PUT', 'DELETE'])
      def get_update_and_delete_user(request, id):
          print("id", id)
          if request.method == 'GET':
              print("fetching user")
              person = [{"name": "danish", "email": "danish@gmail.com"}]
              return Response(person)
          elif request.method == 'PUT':
              print("updating user")
              person = [{"name": "shoaib", "email": "shoaib@gmail.com"}, {"name": "fahad", "email": "fahad@gmail.com"}]
              return Response(person)
          elif request.method == 'DELETE':
              print("deleting user")
              person = [{"name": "fahad", "email": "fahad@gmail.com"}]
              return Response(person)
    ```

   - **Set Up URLs in urls.py**  
     Open `api/urls.py` and add the following code:  
     ```python
        from django.urls import path
        from . import views

        urlpatterns = [
            path("users/", views.create_and_get_all_users),
            path("users/<int:id>", views.get_update_and_delete_user),
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
   Go inside the project `myproject_3` (where you can see the file `manage.py`) and then run the following command to start the Django development server:  
   `python manage.py runserver`

You can now access your GET API at [http://127.0.0.1:8000/api/users/](http://127.0.0.1:8000/api/users/).

# Django App Setup and Server Instructions

## Setup

1. **Install Django Globally**  
   `pip install django`

2. **Create a New Django Project**  
   Use the Django CLI tool `django-admin` to create a new project:  
   `django-admin startproject main`

3. **Rename Project**
   Rename outer folder `main` to `e_commerce`

4. **Create requirements.txt**  
   Inside your project directory (`e_commerce`), create a file named `requirements.txt` and add the following line to specify the Django REST framework:  
   `djangorestframework`

5. **Install Requirements**  
   Install the packages listed in `requirements.txt`:  
   `pip install -r requirements.txt`

6. **Run the Development Server**  
   Go inside the project `e_commerce` (where you can see the file `manage.py`) and then run the following command to start the Django development server:  
   `python manage.py runserver`

7. **Create a new App**
   go inside the folder `e_commerce` and run the following command
   `python manage.py startapp e_commerce_app`

8. **Create APIs**

   - **Update settings.py**  
     Open `main/settings.py` and add `'rest_framework'` to the `INSTALLED_APPS` list:  
     ```python
     INSTALLED_APPS = [
         ...
         'rest_framework',
         'e_commerce_app'
     ]
     ```

   - **Create Model** 
     Open the file `e_commerce_app/models.py` and add the following code
     ```python
      class Product(models.Model):
         name = models.CharField(max_length=256)
         description = models.CharField(max_length=256)
         price = models.FloatField()
         cat_id = models.IntegerField()
         created_at = models.DateTimeField(auto_now_add=True)
      ``` 

   - **Run Migration**  
    run following command to run the migration and create table in sqlite db

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    - **Insert Data Directly in Sqlite**
    ```sql
      INSERT INTO e_commerce_app_product (name, description, price, cat_id, created_at) 
      VALUES ('Smartphone', 'Latest model with 128GB storage', 699.99, 1, '2024-09-25 10:15:00');

      INSERT INTO e_commerce_app_product (name, description, price, cat_id, created_at) 
      VALUES ('Laptop', 'High-performance laptop with 16GB RAM', 1199.99, 1, '2024-09-25 10:20:00');

      INSERT INTO e_commerce_app_product (name, description, price, cat_id, created_at) 
      VALUES ('Fiction Novel', 'A best-selling mystery novel', 14.99, 2, '2024-09-25 10:25:00');

      INSERT INTO e_commerce_app_product (name, description, price, cat_id, created_at) 
      VALUES ('T-Shirt', 'Comfortable cotton t-shirt', 9.99, 3, '2024-09-25 10:30:00');

    ```

   - **Define the GET API in views.py**  
   ```python
      from rest_framework.decorators import api_view
      from rest_framework.response import Response

      from .models import Product

      @api_view(['GET'])
      def get_all_products(request):
          # Use Django's serialize function to convert queryset to JSON format
          products = Product.objects.all()

          # Manually build the list of dictionaries representing each product
          product_list = []
          for product in products:
              product_data = {
                  'id': product.id,
                  'name': product.name,
                  'description': product.description,
                  'price': product.price,
                  'cat_id': product.cat_id,
                  'created_at': product.created_at
              }
              product_list.append(product_data)

          return Response(product_list)
        
    ```

   - **Set Up URLs in urls.py**  
     Open `api/urls.py` and add the following code:  
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path("products/", views.get_all_products),
     ]
     ```

   - **Update Project URLs**  
     Open `main/urls.py` and include the api URLs:  
     ```python
     from django.urls import path, include

     urlpatterns = [
         path('api/', include('e_commerce_app.urls')),
         ...
     ]
     ```

7. **Run the Development Server**  
   Go inside the project `e_commerce` (where you can see the file `manage.py`) and then run the following command to start the Django development server:  
   `python manage.py runserver`

You can now access your GET API at [http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/).

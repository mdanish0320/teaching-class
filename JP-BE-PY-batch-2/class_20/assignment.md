
# Practice Django Project Setup

## Objective
Create and set up three Django projects, each containing different APIs that return static data.

## Step 1: Create Django Projects
Use the following command to create three Django projects:

1. **test_project_1**
   ```bash
   django-admin startproject test_project_1
   ```

2. **test_project_2**
   ```bash
   django-admin startproject test_project_2
   ```

3. **test_project_3**
   ```bash
   django-admin startproject test_project_3
   ```

## Step 2: Create APIs

### In `test_project_1`
- Create a GET API that returns static data.
- API endpoint: `/api/users`
  
### In `test_project_2`
- Create a GET API that returns static data.
- API endpoint: `/report/users`

### In `test_project_3`
- Create two apps:
  1. **app_1**
  2. **app_2**

- For **app_1**:
  - API endpoint: `/api_1/users`

- For **app_2**:
  - API endpoint: `/api_2/users`

### CRUD Application
- Create a simple CRUD application as demonstrated in this [GitHub repository](https://github.com/mdanish0320/teaching-class/tree/master/JP-BE-PY-batch-2/class_20/crud_with_db).

## Notes
- Ensure to run the server for each project using:
  ```bash
  python manage.py runserver
  ```
- Test the APIs using tools like Postman or cURL to verify that they return the expected static data.

_______________________________________________________________________________________
# Library Management System

Create a simple Library Management System that allows users to manage books, authors, and genres. This project involves creating APIs for performing CRUD operations without requiring authentication.

## Database Tables

### Authors
- **id**: Integer (Primary Key)
- **name**: String
- **bio**: Text (optional)

### Genres
- **id**: Integer (Primary Key)
- **name**: String

### Books
- **id**: Integer (Primary Key)
- **title**: String
- **author_id**: Integer 
- **genre_id**: Integer 
- **published_date**: Date (optional)

## Relationships
- Each **Book** can have one **Author**.
- Each **Book** can belong to one **Genre**.
- Each **Author** can write multiple **Books**.
- Each **Genre** can have multiple **Books**.

## CRUD Operations

### Authors API
- **GET** `/authors/` - List all authors
- **POST** `/authors/` - Create a new author
- **GET** `/authors/{id}/` - Retrieve a specific author
- **PUT** `/authors/{id}/` - Update an existing author
- **DELETE** `/authors/{id}/` - Delete an author

### Genres API
- **GET** `/genres/` - List all genres
- **POST** `/genres/` - Create a new genre
- **GET** `/genres/{id}/` - Retrieve a specific genre
- **PUT** `/genres/{id}/` - Update an existing genre
- **DELETE** `/genres/{id}/` - Delete a genre

### Books API
- **GET** `/books/` - List all books - **filter by query string author_id, genre_id, title, published_date**
- **POST** `/books/` - Create a new book
- **GET** `/books/{id}/` - Retrieve a specific book
- **PUT** `/books/{id}/` - Update an existing book
- **DELETE** `/books/{id}/` - Delete a book

## Implementation Steps
1. **Create Models**: Define the Author, Genre, and Book models in Django.
2. **Migrations**: Run migrations to create the database tables.
3. **Create Views**: Use functional-based views to handle the CRUD operations for each model.
4. **URLs**: Map the views to appropriate URLs in `urls.py`.
5. **Test APIs**: Use tools like Postman or cURL to test the APIs.

## NOTE
1. **Filter**: Apply filters by query string author_id, genre_id, title, published_date
2. **/books/**: This API should return joined data (i.e replace author_id with the auther_name, genre_id with genre_name) without using the join query. hint:[filtering-objects-using-in-clause](https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_20/common_django_orm_usage.md#5-filtering-objects-using-in-clause)
and
[values-list](https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_20/common_django_orm_usage.md#13-values-and-values-list)

```python
from django.forms.models import model_to_dict

category_id = products_objects.values_list('category_id', flat=True)
categories = category_model.objects.filter(id__in=category_id).all()
products = products_objects.all()
for product in products:
   for category in categories:
       if product.category_id == category.id:
           data = {**model_to_dict(product), "category": model_to_dict(category)}
           all_data.append(data)

output:
[
    {
        "id": 1,
        "name": "product 1",
        "description": null,
        "quantity": 10,
        "price": 100,
        "category_id": 1,
        "category": {
            "id": 1,
            "name": "cat_1",
            "description": null,
            "status": null
        }
    },
    {
        "id": 2,
        "name": "product 2",
        "description": null,
        "quantity": 10,
        "price": 100,
        "category_id": 2,
        "category": {
            "id": 2,
            "name": "toy",
            "description": null,
            "status": null
        }
    }
]
```

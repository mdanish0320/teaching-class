# Django App Setup and Server Instructions

## Setup

1. **Install Django Globally**  
   `pip install django`

2. **Create a New Django Project**  
   Use the Django CLI tool `django-admin` to create a new project:  
   `django-admin startproject main`

3. **Rename Project**
   Rename outer folder `main` to `crud_with_db`

4. **Create requirements.txt**  
   Inside your project directory (`e_commerce`), create a file named `requirements.txt` and add the following line to specify the Django REST framework:  
   `djangorestframework`

5. **Install Requirements**  
   Install the packages listed in `requirements.txt`:  
   `pip install -r requirements.txt`

6. **Run the Development Server**  
   Go inside the project `e_commerce` (where you can see the file `manage.py`) and then run the following command to start the Django development server:  
   `python manage.py runserver`

7. - **Create a new App**
   Go inside the folder `e_commerce` and run the following command
   `python manage.py startapp e_commerce`


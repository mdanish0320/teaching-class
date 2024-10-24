Here's an improved and properly structured guide on common Django ORM usage. The guide has been organized for clarity, with consistent formatting, clear headings, and concise explanations.

# Common Django ORM Usage Guide

Django's Object-Relational Mapping (ORM) allows developers to interact with the database using Python code, providing a high-level abstraction for database operations. Below are some common ORM queries and their usage.

## 1. Retrieving All Objects
To retrieve all instances of a model, use:
```python
Model.objects.all()
```
**Description**: This returns a queryset containing all objects of the specified model.

## 2. Filtering Objects
To filter objects based on specific conditions:
```python
Model.objects.filter(field_name=value)
```
**Description**: This returns a queryset containing all objects that match the specified filter conditions.

### 2.1 Filtering with Case-Insensitive Search
To search for objects with names that contain a specific term:
```python
search_term = data['search']  # Get the search term from the JSON
# Query products using case-insensitive search
products = Product.objects.filter(name__icontains=search_term)
```
**Description**: This returns all products where the `name` field contains the `search_term`, ignoring case.

### 2.2 Filtering with Case-Insensitive Starts With
To filter objects where the name starts with a specific term:
```python
search_term = data['search']  # Get the search term from the JSON
# Query products using case-insensitive starts with
products = Product.objects.filter(name__istartswith=search_term)
```
**Description**: This returns all products where the `name` field starts with the `search_term`, ignoring case.

## 3. Getting a Single Object
To retrieve a single object by its primary key:
```python
obj = Model.objects.get(pk=1)
```
**Description**: This retrieves the object with the specified primary key. It raises a `DoesNotExist` exception if no object is found and a `MultipleObjectsReturned` exception if multiple objects are found.

## 4. Filtering Objects Using the IN Clause
To filter objects using a list of IDs:
```python
product_ids = data['ids']  # Get the list of product IDs from the JSON
# Query products using the IN clause
products = Product.objects.filter(id__in=product_ids)
```
**Description**: This returns a queryset containing all products whose IDs are in the `product_ids` list.

## 5. Creating a New Object
To create and save a new instance of a model:
```python
obj = Model(field_name=value)
obj.save()
```
**Description**: This creates a new object and saves it to the database.

### 5.1 Creating an Object Using `create`
You can also create and save an object in one step:
```python
obj = Model.objects.create(field_name=value)
```
**Description**: This creates and saves a new instance of the model.

### 5.2 Creating an Object with Multiple Fields
To create an object using a dictionary of data:
```python
obj = Model.objects.create(**data)
```
**Description**: This creates and saves a new instance of the model using the provided data dictionary.

## 6. Updating Objects
To update an existing object:
```python
obj = Model.objects.get(pk=1)
obj.field_name = new_value
obj.save()
```
**Description**: This retrieves an object, updates its fields, and saves the changes to the database.

## 7. Deleting Objects
To delete an existing object:
```python
obj = Model.objects.get(pk=1)
obj.delete()
```
**Description**: This retrieves the object and deletes it from the database.

## 8. Counting Objects
To get the total number of objects in the database:
```python
count = Model.objects.count()
```
**Description**: This returns the total count of all objects for the specified model.

## 9. Ordering Results
To order query results by a specific field:
```python
Model.objects.order_by('field_name')
```
**Description**: This retrieves all objects ordered by the specified field. Use a minus sign (`-`) before the field name to order in descending order (e.g., `-field_name`).

## 10. Values and Values List
To retrieve specific fields from objects:
```python
# Using values
category_data = CategoryModel.objects.values('id')

# Using values_list
category_ids = CategoryModel.objects.values_list('id', flat=True)

# Querying products based on category IDs
products = ProductModel.objects.filter(id__in=category_ids).all()
```
**Description**: 
- `values()` returns a queryset of dictionaries with the specified fields.
- `values_list()` returns a queryset of tuples (or a flat list if `flat=True`), providing a more straightforward way to extract a single field.

## Summary
This guide provides an overview of common operations using Django's ORM. Understanding these queries will help you interact with your database efficiently and effectively in Django applications. For more advanced usage and features, refer to the official Django documentation.

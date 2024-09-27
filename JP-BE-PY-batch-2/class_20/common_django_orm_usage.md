
# Common Django ORM Usage

Django's Object-Relational Mapping (ORM) allows interaction with the database using Python code. Below are some common ORM queries and their usage:

## 1. Retrieving All Objects
```python
Model.objects.all()
```
This retrieves all instances of a model.

## 2. Filtering Objects
```python
Model.objects.filter(field_name=value)
```
This returns a queryset containing all objects that match the specified filter conditions.


## 3. Filtering Objects
```python
search_term = data['search']  # Get the search term from the JSON
# Query products using the LIKE query
products = Product.objects.filter(name__icontains=search_term)
```
This returns a queryset containing all objects that match the specified filter conditions insensitive.

## 4. Getting a Single Object
```python
Model.objects.get(pk=1)
```
This retrieves a single object by its primary key. If no object is found, it raises a `DoesNotExist` exception, and if multiple objects are found, it raises a `MultipleObjectsReturned` exception.


## 5. Filtering Objects Using IN Clause
```python
product_ids = data['ids']  # Get the list of product IDs from the JSON
# Query products using the IN clause
products = Product.objects.filter(id__in=product_ids)
```
This returns a queryset containing all objects that match the specified filter conditions.

## 6. Creating a New Object
```python
obj = Model(field_name=value)
obj.save()
```
This creates a new instance of a model and saves it to the database.

## 7. Creating an Object Using `create`
```python
obj = Model.objects.create(field_name=value)
```
This creates and saves a new instance of a model in one step.

## 8. Creating an Object Using `create`
```python
obj = Model.objects.create(**data)
```
This creates and saves a new instance of a model in one step.

## 9. Updating Objects
```python
obj = Model.objects.get(pk=1)
obj.field_name = new_value
obj.save()
```
This retrieves an object and updates its fields before saving the changes to the database.

## 10. Deleting Objects
```python
obj = Model.objects.get(pk=1)
obj.delete()
```
This retrieves an object and deletes it from the database.

## 11. Counting Objects
```python
count = Model.objects.count()
```
This returns the total number of objects in the database for the model.

## 12. Ordering Results
```python
Model.objects.order_by('field_name')
```
This retrieves all objects ordered by a specified field. You can use a minus sign (`-`) to order in descending order (e.g., `-field_name`).

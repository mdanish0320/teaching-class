
# Common Django Model Fields

## CharField
- **SQL Equivalent:** `varchar(200) NOT NULL`
- **Django Example:**
  ```python
  name = models.CharField(max_length=200)
  ```

## TextField
- **SQL Equivalent:** `TEXT NULL`
- **Django Example:**
  ```python
  description = models.TextField(blank=True, null=True)
  ```

## ForeignKey
- **SQL Equivalent:** `cat_id INT NOT NULL`
- **Django Example:**
  ```python
  cat_id = models.ForeignKey('Category', on_delete=models.CASCADE)  # Assuming 'Category' is another model
  ```

## DateTimeField
- **SQL Equivalent:** `DATETIME DEFAULT NOW()`
- **Django Example:**
  ```python
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  ```

## IntegerField
- **SQL Equivalent:** `status enum(1, 2, 3) default 1`
- **Django Example:**
  ```python
  STATUS_CHOICES = [
      (1, 'Status 1'),
      (2, 'Status 2'),
      (3, 'Status 3'),
  ]
  status = models.IntegerField(choices=STATUS_CHOICES, default=1)
  ```

## EmailField
- **SQL Equivalent:** `varchar UNIQUE and INDEX`
- **Django Example:**
  ```python
  email = models.EmailField(unique=True)
  ```

## Complete Example Model
Here’s how you might combine these fields into a Django model:

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cat_id = models.ForeignKey('Category', on_delete=models.CASCADE)  # Adjust as necessary
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = [
        (1, 'Status 1'),
        (2, 'Status 2'),
        (3, 'Status 3'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
```


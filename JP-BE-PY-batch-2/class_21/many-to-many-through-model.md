In Django, a **custom through model** is an intermediary table that allows you to add extra fields to a many-to-many relationship. By default, Django automatically creates an intermediate table to manage many-to-many relationships between two models, but this table is hidden from the user and contains only the foreign keys that reference the related models.

However, if you want to add additional information to the many-to-many relationship (e.g., a `status` field, `created_at` timestamps, or other custom data), you need to define this intermediate table explicitly using a **custom through model**.

### Why Use a Custom Through Model?

A custom through model allows you to:
1. Add additional fields to the relationship (e.g., `status`, `created_at`, etc.).
2. Control the intermediate table's behavior explicitly (e.g., validation, unique constraints, custom methods).

### How to Define a Custom Through Model

To define a custom through model, follow these steps:

1. **Create the Through Model**: This is the table that will store the relationship between the two models along with any additional fields.
2. **Specify the `through` Attribute**: In the `ManyToManyField`, you specify the `through` parameter to use the custom model.

### Example:

Let’s say you have `Product` and `Category` models. You want to track a `status` for each relationship between a product and a category. Here's how you can do it:

#### Step 1: Define the Custom Through Model

```python
from django.db import models

# Custom through model to add fields to the relationship
class ProductCategory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)  # Custom field
    created_at = models.DateTimeField(auto_now_add=True)  # Custom field
    updated_at = models.DateTimeField(auto_now=True)  # Custom field

    class Meta:
        unique_together = ('product', 'category')  # Ensure the relationship is unique
```

#### Step 2: Define the `Product` and `Category` Models

In the `Product` model, the `category` field will use the `through` parameter to specify that the relationship should go through the `ProductCategory` model.

```python
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, through='ProductCategory')  # Specify the custom through model
```

### Step 3: Working with the Custom Through Model

You can't use the `set()`, `add()`, or `remove()` methods with a custom through model. Instead, you need to work with the through model directly to manage the relationship.

#### Adding a Relationship:
To add a new relationship between `Product` and `Category` and include the `status` field:

```python
# Create product and category instances
product = Product.objects.create(name='Laptop')
category = Category.objects.create(name='Electronics')

# Add the relationship using the through model
ProductCategory.objects.create(product=product, category=category, status='active')
```

#### Querying the Relationship:
To retrieve the relationship and access the additional fields (e.g., `status`):

```python
# Query the through model to get the relationship and additional fields
product_categories = ProductCategory.objects.filter(product=product)

for pc in product_categories:
    print(pc.category.name, pc.status)
```

### Benefits of Using a Custom Through Model:

- **Additional Fields**: You can store additional information about the relationship (e.g., `status`, `created_at`, `priority`).
- **More Control**: You can define custom validation, methods, or constraints on the intermediary model.
- **Flexibility**: You can handle more complex relationships that involve data beyond just the foreign keys.

### Summary:

- **Default Many-to-Many**: Django creates an automatic join table without any extra fields.
- **Custom Through Model**: You explicitly define the intermediate table and can add custom fields, but you need to manage the relationship manually using the custom model.

This approach is useful when the relationship itself has properties (e.g., `status`, `created_at`) that need to be stored and managed.
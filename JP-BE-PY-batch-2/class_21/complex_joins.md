To achieve the SQL query:

```sql
SELECT * 
FROM orders o 
INNER JOIN products p ON o.product_id = p.id 
INNER JOIN customers c ON o.customer_id = c.id;
```

using Django ORM, we need to model the relationships between the `Orders`, `Products`, and `Customers` tables. The query involves foreign key relationships, so let’s define the minimal models, serializer, and an efficient ORM query to match this SQL.

### 1. Models

Define the minimal models to represent `Orders`, `Products`, and `Customers`. Each order is related to a product and a customer via foreign keys.

```python
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
```

### 2. Serializer

Define a minimal serializer to serialize the data of `Orders`, `Products`, and `Customers`. We use `serializers.Serializer` and manually handle the relationships.

```python
from rest_framework import serializers
from .models import Order, Product, Customer

class OrderSerializer(serializers.Serializer):
    product_name = serializers.CharField(source='product.name')
    customer_name = serializers.CharField(source='customer.name')
    quantity = serializers.IntegerField()
    order_date = serializers.DateTimeField()
    
    def to_representation(self, instance):
        return {
            'product_name': instance.product.name,
            'customer_name': instance.customer.name,
            'quantity': instance.quantity,
            'order_date': instance.order_date
        }
```

- `product_name` and `customer_name` are sourced from the related `Product` and `Customer` models using the `source` argument.
- `to_representation` ensures custom output format when serialized.

### 3. ORM Query

To efficiently perform the query that mimics your SQL `INNER JOIN` in Django ORM, you can use the `select_related` method to reduce the number of queries. This method retrieves related objects in a single query, which is highly efficient for foreign key relationships.

```python
from .models import Order

# Efficient ORM query using select_related for foreign key relationships
orders = Order.objects.select_related('product', 'customer').all()

# Serialize the result
serializer = OrderSerializer(orders, many=True)
return Response(serializer.data)
```

### How the Query Works:

- `select_related('product', 'customer')`: This performs an SQL join internally between the `Order`, `Product`, and `Customer` models, avoiding the N+1 query problem.
- `.all()`: Fetches all orders.
  
This ORM query corresponds to:

```sql
SELECT *
FROM orders o
INNER JOIN products p ON o.product_id = p.id
INNER JOIN customers c ON o.customer_id = c.id;
```

### 4. Putting It Together in a View

Here’s a complete function-based view (FBV) to fetch and return the order data with an efficient query:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

@api_view(['GET'])
def get_orders(request):
    # Efficient ORM query
    orders = Order.objects.select_related('product', 'customer').all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
```

### Summary:

- **Models**: We define `Order`, `Product`, and `Customer` with foreign key relationships.
- **Serializer**: The `OrderSerializer` manually handles related fields (`product_name`, `customer_name`).
- **ORM Query**: We use `select_related()` for efficient querying and avoid multiple DB hits.

This setup mimics the SQL `INNER JOIN` query and is optimized for Django's ORM.
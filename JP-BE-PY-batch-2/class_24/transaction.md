### 1. Transaction Management with `@transaction.atomic` Decorator

The `@transaction.atomic` decorator wraps the entire API view in a transaction. If an exception occurs anywhere in the view, all database operations within the transaction are rolled back. On successful execution, the transaction is committed on API response.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from .models import Order, OrderItem  # Ensure your models are correctly imported

class OrderView(APIView):
    @transaction.atomic
    def post(self, request):
        try:
            # Create an order
            order = Order.objects.create(customer=request.data['customer'], total=request.data['total'])
            
            # Add order items
            for item in request.data['items']:
                OrderItem.objects.create(order=order, product_id=item['product_id'], quantity=item['quantity'])

            return Response({'status': 'success', 'order_id': order.id})

        except Exception as e:
            # An exception will trigger a rollback
            return Response({'status': 'error', 'message': str(e)}, status=400)
```

### 2. Manual Transaction Management Using `transaction.atomic` Decorator

In cases where you need more granular control over which parts of your view should be executed within a transaction, you can use `transaction.atomic` with explicit commit and rollback points.

```python
from django.db import transaction
from rest_framework.response import Response

@transaction.atomic
def some_view(request):
    try:
        # Perform some database operations
        product = Product.objects.create(name="Test Product")
        
        # Manually commit the transaction if necessary
        transaction.commit()

        return Response({'status': 'success'})

    except Exception as e:
        # Rollback the transaction in case of an error
        transaction.rollback()
        return Response({'status': 'error', 'message': str(e)}, status=400)
```

### 3. Transaction Management Using `with transaction.atomic()` Context Manager

The `with transaction.atomic()` context manager allows you to control transaction scope within a specific block of code, offering flexibility in more complex views.

```python
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response

class OrderView(APIView):
    def post(self, request):
        try:
            with transaction.atomic():
                # Create an order
                order = Order.objects.create(customer=request.data['customer'], total=request.data['total'])

                # Add order items
                for item in request.data['items']:
                    OrderItem.objects.create(order=order, product_id=item['product_id'], quantity=item['quantity'])

            return Response({'status': 'success', 'order_id': order.id})

        except Exception as e:
            # Any exception will trigger a rollback
            return Response({'status': 'error', 'message': str(e)}, status=400)
```

### views.py

```python
# views.py
from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerialzer

class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category")
        .prefetch_related("supplier")
        .all()
    )
    serializer_class = ProductSerialzer

    def filter_queryset(self, queryset):
        """
        Override the filter_queryset method to apply custom filtering based on query parameters.

        Args:
            queryset: The initial queryset of Product instances.

        Returns:
            A filtered queryset based on the provided query parameters.
        """
        filter_queryset = super().filter_queryset(queryset)
        qp = self.request.query_params

        # Filter by Supplier ID
        if qp.get("supplier_id") is not None:
            filter_queryset = filter_queryset.filter(supplier__id=qp.get("supplier_id"))

        # Filter by Category ID
        if qp.get("category_id") is not None:
            filter_queryset = filter_queryset.filter(category__id=qp.get("category_id"))

        # Filter by Exact Name
        if qp.get("name") is not None:
            filter_queryset = filter_queryset.filter(name=qp.get("name"))

        # Filter by Name Like
        if qp.get("name_like") is not None:
            filter_queryset = filter_queryset.filter(
                name__icontains=qp.get("name_like")
            )

        # Filter by Name Starting With
        if qp.get("name_start") is not None:
            filter_queryset = filter_queryset.filter(
                name__istartswith=qp.get("name_start")
            )

        return filter_queryset
```

### Key Features

- **Queryset Optimization:** The queryset uses `select_related` for the `category` and `prefetch_related` for `supplier` to minimize database queries and enhance performance.
  
- **Custom Filtering:** The `filter_queryset` method is overridden to allow filtering of `Product` instances based on specific query parameters provided in the request.

### Filtering Options

- **Filter by Supplier ID:** Pass `supplier_id` as a query parameter.
  
- **Filter by Category ID:** Use `category_id` to filter products by their associated category.
  
- **Filter by Exact Name:** Use `name` to get products that exactly match the provided name.
  
- **Filter by Name Like:** Use `name_like` to find products with names containing the specified substring.
  
- **Filter by Name Starting With:** Use `name_start` to filter products whose names start with the given string.

## Conclusion

The `ProductModelViewSet` provides a flexible and efficient way to manage `Product` instances through a RESTful API. By overriding the `filter_queryset` method, you can easily implement custom filtering based on user-defined parameters, enhancing the user experience and making data retrieval more efficient.


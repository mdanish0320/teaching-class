# Product Filtering in Django REST Framework

This project implements a filtering system for a Product API using Django REST Framework and `django-filter`. The following sections outline the setup, filtering options, and usage examples.

## Filters Implementation

### filters.py

This module defines the `ProductFilter`, which allows for filtering `Product` instances based on various fields, including supplier and category.

```python
# filters.py
from django_filters import rest_framework as filters
from app.models import Product

class ProductFilter(filters.FilterSet):
    supplier_id = filters.NumberFilter(field_name="supplier__id")
    supplier_name = filters.CharFilter(
        field_name="supplier__name", lookup_expr="icontains"
    )
    category_id = filters.NumberFilter(field_name="category__id")
    category_name = filters.CharFilter(
        field_name="category__name", lookup_expr="icontains"
    )
    name = filters.CharFilter(field_name="name", lookup_expr="exact")
    name_like = filters.CharFilter(field_name="name", lookup_expr="icontains")
    name_start = filters.CharFilter(field_name="name", lookup_expr="istartswith")
    price_gt = filters.NumberFilter(field_name="price", lookup_expr="gt")
    price_lt = filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Product
        fields = [
            "supplier_id",
            "supplier_name",
            "category_id",
            "category_name",
            "name",
            "name_like",
            "name_start",
            "price_gt",
            "price_lt",
        ]
```

## View Implementation

### views.py

This section demonstrates the integration of the `ProductFilter` into a `ModelViewSet` for handling API requests.

```python
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Product
from app.serializers import ProductSerialzer
from ..filters import ProductFilter

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.select_related("category").prefetch_related("supplier").all()
    serializer_class = ProductSerialzer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
```

## Configuration

### settings.py

To enable filtering in your Django REST Framework application, ensure you have the following settings:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # Include other filter backends if needed
    ),
}
```

## Accessing Your API

You can access your Product API and filter results using the following query parameters without the need for HTML forms:

- **Filter by Supplier ID:**  
  `/app_adv_filter/product/?supplier_id=1`
  
- **Filter by Supplier Name:**  
  `/app_adv_filter/product/?supplier_name=Acme`
  
- **Filter by Category ID:**  
  `/app_adv_filter/product/?category_id=2`
  
- **Filter by Category Name:**  
  `/app_adv_filter/product/?category_name=Electronics`
  
- **Filter by Exact Name:**  
  `/app_adv_filter/product/?name=Product A`
  
- **Filter by Name Like:**  
  `/app_adv_filter/product/?name_like=Product`
  
- **Filter by Name Starting With:**  
  `/app_adv_filter/product/?name_start=Prod`
  
- **Filter by Price Greater Than:**  
  `/app_adv_filter/product/?price_gt=100`
  
- **Filter by Price Less Than:**  
  `/app_adv_filter/product/?price_lt=500`



### 1. **Configure Pagination in Settings**
First, configure the pagination settings in your `settings.py` file. DRF provides built-in pagination classes, such as `PageNumberPagination`, `LimitOffsetPagination`, and `CursorPagination`.

For example, to use `PageNumberPagination`:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10  # Adjust this number as per your requirement
}
```

### 2. **Use Pagination in Class-Based Views**
DRF’s generic views or viewsets automatically support pagination if you've configured it in your `settings.py`. Here's how you can use pagination with a **ListAPIView** or any other generic views like **ListCreateAPIView**.

#### Example using `ListAPIView`:
```python
from rest_framework.generics import ListAPIView
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListView(ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```
In this case, pagination is automatically applied as DRF will pick up the pagination settings from `settings.py`.

### 3. **Custom Pagination on a Per-View Basis**
If you want to customize pagination for a particular view, you can specify a pagination class directly in the view:

#### Example using `PageNumberPagination` for a specific view:
```python
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import MyModel
from .serializers import MyModelSerializer

class CustomPagination(PageNumberPagination):
    page_size = 5  # Customize page size for this view
    page_size_query_param = 'page_size'
    max_page_size = 100

class MyModelListView(ListAPIView): # or class MyModelViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    pagination_class = CustomPagination
```


### 4. **Customizing Pagination Response**
If you want to modify the pagination response, you can override the `get_paginated_response` method of the pagination class.

#### Example:
```python
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
```

This will customize the paginated response with next/previous links and the count of total records.

### Conclusion
- **Global Pagination**: Set in `settings.py`.
- **Per-View Pagination**: Define a custom `pagination_class` in a specific view.
- Pagination is automatically handled by generic views like `ListAPIView` and `ModelViewSet`.

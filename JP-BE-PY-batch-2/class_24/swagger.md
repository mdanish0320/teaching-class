### Step 1: Install `drf-yasg`

First, you need to install the `drf-yasg` package. You can do this using pip:

```bash
pip install drf-yasg
```

### Step 2: Update `settings.py`

Add `drf_yasg` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'drf_yasg',
    ...
]
```

### Step 3: Create your API View

Create a class-based view using DRF's `APIView` or any of its subclasses (like `ListAPIView`, `RetrieveAPIView`, etc.). Here's an example of a simple class-based view:

```python
class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.select_related("category").prefetch_related("supplier").all()
    serializer_class = ProductSerialzer
```

### Step 4: Configure Swagger

Now, you need to configure Swagger in your `main/urls.py`:

```python
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ...
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ...
]
```

### Step 5: Run the Server

Run your Django server:

```bash
python manage.py runserver
```

### Step 6: Access Swagger UI

You can access the Swagger UI by navigating to:

```
http://localhost:8000/swagger/
```

And for ReDoc, go to:

```
http://localhost:8000/redoc/
```
# File Uploads in Django REST Framework

This guide outlines the steps for handling file uploads and displaying images in your Django REST Framework application.

## Step 1: Uploading Files

To enable file uploads, follow these steps:

1. **Update Your Model**: 
   Add a file field to your model. For example:
   ```python
   from django.db import models

   class Product(models.Model):
       image = models.FileField(upload_to="products/", null=True, blank=True)
       # Add other fields as needed
   ```

2. **Modify Your Views**: 
   In your `views.py`, ensure your viewset is set up to handle file uploads:
   ```python
   from rest_framework import viewsets
   from rest_framework.parsers import MultiPartParser, FormParser
   from .models import Product
   from .serializers import ProductSerializer

   class ProductViewSet(viewsets.ModelViewSet):
       queryset = Product.objects.all()
       serializer_class = ProductSerializer
       parser_classes = (MultiPartParser, FormParser)  # Enable file upload handling
   ```

## Step 2: Displaying Images

To configure your project for serving static and media files, follow these steps:

1. **Static Files Configuration**:
   Add the following settings to your `settings.py`:
   ```python
   import os

   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   ```

2. **Media Files Configuration (for uploads)**:
   Add the following settings for handling media files:
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

## Step 3: Serving Media Files in Development

**Important**: The following configuration is not recommended for production environments.

To serve media files during development, add the following to the end of your `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your url patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

This setup allows your application to serve media files directly from the specified `MEDIA_ROOT` when in development mode.

---

By following these steps, you can successfully handle file uploads and serve images in your Django REST Framework application. For further customization or deployment considerations, refer to the [Django documentation](https://docs.djangoproject.com/en/stable/howto/static-files/).
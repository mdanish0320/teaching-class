### 1. **Using APIView** (Manual CRUD Implementation)

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### 2. **Using DRF Generics**

```python
# views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### 3. **Using DRF ModelViewSet**

```python
# views.py
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### **Serializers for All Views**

```python
# serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

### **URLs**

For **APIView** and **Generics**, you need to manually define routes and for **ViewSet**, DRF provides routers to automatically create the routes:

```python
# urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductAPIView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
from .views import ProductViewSet

urlpatterns = [
    # APIView URLs
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),

    # Generics URLs
    path('generic-products/', ProductListCreateAPIView.as_view(), name='generic-product-list'),
    path('generic-products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='generic-product-detail'),
]

router = DefaultRouter()
router.register(r'viewset-products', ProductViewSet, basename='viewset-product')

urlpatterns += router.urls
```

### **Summary:**
- **APIView**: More control but more code. You manually handle CRUD operations.
- **Generics**: Simplifies the CRUD operations with minimal code.
- **ViewSet**: Further abstraction; CRUD logic is automatically handled, with route generation via routers.
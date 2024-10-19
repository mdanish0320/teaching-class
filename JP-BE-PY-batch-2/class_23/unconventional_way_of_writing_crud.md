## Unconventional Solutions for Displaying and Storing Relational Data Without Overriding ModelViewSet Methods

When working with relational data in Django Rest Framework (DRF), managing complex relationships and handling foreign key or many-to-many fields can often involve customizing `ModelViewSet` methods, like `create()` or `update()`. However, there are more unconventional ways to streamline displaying and storing relational data without needing to override the default behaviors of `ModelViewSet` methods. This article explores a creative approach to managing relational fields in DRF by renaming and simplifying these fields in the `models.py` and `serializers.py` files.

### Scenario Overview: Renaming Relational Fields Manually

In this approach, we will explore how to rename foreign key and many-to-many fields within a Django model and then structure the serializers in a way that allows for seamless input and output of related data without complex method overrides. We’ll use the following model:

```python
# models.py
class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE, db_column="category_id"
    )
    supplier_id = models.ManyToManyField(Supplier, related_name="products", db_column="supplier_id")

    def __str__(self):
        return self.name
```

Here, we’ve manually renamed the relational fields to match our database column names (`user_id`, `category_id`, and `supplier_id`). By doing so, we don’t need to override the `ModelViewSet` methods for basic operations such as creating or updating a `Product`.

### Step 1: Simplifying Serializers for Relational Fields

Our next step is to configure serializers that handle both the display and input of relational data. For input, we want to use the primary key (ID) of related models, while for output, we display the full related objects.

```python
# serializers.py
class ProductSerializer(serializers.ModelSerializer):
    # Write-only fields for inputting IDs
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Supplier.objects.all(), write_only=True, allow_empty=False)

    # Read-only fields for displaying the full related objects
    user = UserSerializer(source='user_id', read_only=True)
    category = CategorySerializer(source='category_id', read_only=True)
    supplier = SupplierSerializer(source='supplier_id', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'user_id', 'user', 'name', 'description', 'price', 'category_id', 'category', 'supplier_id', 'supplier']
```

### Step 2: Key Benefits of this Approach

1. **Avoiding Overriding Methods:**
   By carefully structuring both the model fields and serializers, we avoid the need to manually override methods like `create()` and `update()` in our `ModelViewSet`. DRF handles the conversion between relational IDs and objects for us, automatically managing the complexity.

2. **Separation of Input and Output Logic:**
   The `write_only=True` and `read_only=True` flags in the serializer fields help separate how relational data is handled for input versus how it is displayed in the API responses. For input, only the primary keys (IDs) are accepted, while for output, full serialized objects are shown.

3. **Improved Readability and Flexibility:**
   This method improves the readability of the code by clearly differentiating how the relational data should be handled in different contexts (input vs. output). It also offers flexibility in handling various related fields, whether they are foreign keys or many-to-many relationships.

### Step 3: Integrating with `ModelViewSet`

Here’s the beauty of this approach: The integration with the `ModelViewSet` requires no special handling. You can use a standard `ModelViewSet` to interact with the `Product` model and let DRF’s default behavior manage the creation, updating, and retrieval of data.

```python
# views.py
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

Since the serializer already handles the complexities of relational data, the `ModelViewSet` can remain simple, and there’s no need to override its default behavior. DRF’s automatic viewset methods will handle creating and updating the `Product` model, converting between IDs and related objects without extra intervention.

### Step 4: Testing the API

Let’s look at how this setup behaves when interacting with the API. When creating a `Product`, you only need to supply the related IDs (for `user_id`, `category_id`, and `supplier_id`):

**POST Request:**
```json
{
    "user_id": 1,
    "name": "Sample Product",
    "description": "This is a sample product.",
    "price": "100.00",
    "category_id": 2,
    "supplier_id": [3, 4]
}
```

**Response:**
```json
{
    "id": 5,
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    },
    "name": "Sample Product",
    "description": "This is a sample product.",
    "price": "100.00",
    "category": {
        "id": 2,
        "name": "Electronics"
    },
    "supplier": [
        {
            "id": 3,
            "name": "Supplier One"
        },
        {
            "id": 4,
            "name": "Supplier Two"
        }
    ]
}
```

As you can see, relational fields are handled cleanly. The request uses relational IDs, and the response provides full details for related objects.

### Conclusion

This unconventional solution simplifies working with relational data by:
- Using `PrimaryKeyRelatedField` for inputting related IDs.
- Using nested serializers for displaying full related objects.
- Avoiding the need to override `ModelViewSet` methods.

By leveraging DRF’s serializers to handle input and output differently, you can easily manage relational data without additional customizations. This keeps the codebase clean and maintainable while allowing flexibility in displaying and storing related models.
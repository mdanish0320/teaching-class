# Handling One-to-One and Many-to-Many Relationships in Django: A Step-by-Step Guide

In Django, dealing with **One-to-One** and **Many-to-Many** relationships between models is common, especially when building APIs for e-commerce or similar platforms. This article explores how to handle such relationships while creating and displaying product data with related categories and suppliers.

We will go through two solutions:
1. A more conventional approach that requires overriding the `create` method.
2. An unconventional approach that renames model column names to simplify the logic.

### Scenario
We have a `Product` model with:
- A **foreign key** relationship to a `Category` (many-to-one).
- A **many-to-many** relationship with `Supplier`.
- A **foreign key** relationship with `User` to track the creator.

Our goal is:
- **Display API:** List products with related `Category`, `Supplier`, and `User` data.
- **Create API:** Handle inputs for creating a product, including selecting `category_id` and `supplier_ids`.

### Models Setup

#### Solution 1: Conventional Approach with Overridden `create` Method

**`models.py`**
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    supplier = models.ManyToManyField(Supplier, related_name="products")

    def __str__(self):
        return self.name
```

In this approach:
- **`category`** is a foreign key linking to `Category`.
- **`supplier`** is a many-to-many field linking to `Supplier`.
- **`user`** tracks the creator of the product.

#### Serializer for Product Model

**`serializers.py`**
```python
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    # Fields for inputting IDs (write-only)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        many=True,
        allow_empty=False,
        write_only=True,
    )

    class Meta:
        model = Product
        fields = "__all__"
```

In this setup:
- **Read-only fields** like `category`, `supplier`, and `user` are included for display purposes.
- **Write-only fields** like `category_id` and `supplier_id` allow users to input related object IDs during product creation.

#### Overriding the `create` Method

**`views.py`**
```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer):
        # Extract supplier and category IDs from validated data
        supplier = serializer.validated_data.pop("supplier_id")
        category = serializer.validated_data.pop("category_id")

        # Create the product instance with the provided category and user
        product = serializer.save(category=category, user=self.request.user)

        # Assign the selected suppliers to the product
        product.supplier.set(supplier)
        return product
```

The `perform_create` method is overridden to handle **many-to-many relationships** (i.e., `supplier`). We extract the `supplier_id` from the request, create the `Product`, and then set the `supplier` IDs on the newly created product.

### Listing Product Data Example
Here’s how the API response will look for the listing:

```json
[
    {
        "id": 1,
        "category": {
            "id": 1,
            "name": "toys",
            "description": ""
        },
        "supplier": [
            {
                "id": 1,
                "name": "toy supplier",
                "contact_email": "dan@gmail.com",
                "phone_number": ""
            }
        ],
        "user": {
            "id": 1,
            "username": "danish"
        },
        "name": "product 1",
        "description": "",
        "price": "100.00"
    }
]
```

In this response, all relational data for `category`, `supplier`, and `user` is displayed.

#### Solution 2: Unconventional Approach (Renaming Model Column Names)

Instead of overriding the `create` method, you can rename model columns to match input JSON keys for categories and suppliers. This makes the input structure more consistent but breaks conventional naming conventions in Django.

**`models.py`**
```python
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

In this case, the `category_id` and `supplier_id` columns are renamed to align with input data, but they break naming convention.

#### Serializer for Product Model

**`serializers.py`**
```python
class ProductSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Supplier.objects.all(), write_only=True, allow_empty=False)

    user = UserSerializer(source='user_id', read_only=True)
    category = CategorySerializer(source='category_id', read_only=True)
    supplier = SupplierSerializer(source='supplier_id', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'user_id', 'user', 'name', 'description', 'price', 'category_id', 'category', 'supplier_id', 'supplier']
```

In this unconventional solution:
- The `category_id` and `supplier_id` fields match the expected input fields, so no need to override the `create` method.
- Full objects are still displayed for related models in the response (`category`, `supplier`, `user`).

### Key Takeaways
1. **Solution 1** (Conventional): Adheres to best practices but requires overriding the `create` method to handle many-to-many relationships.
2. **Solution 2** (Unconventional): Renames relational fields to match input structure, avoiding the need to override, but breaks naming conventions.

Both approaches work well depending on your preference for maintaining Django conventions versus ease of handling input data. Choose the solution that best fits your project’s requirements!
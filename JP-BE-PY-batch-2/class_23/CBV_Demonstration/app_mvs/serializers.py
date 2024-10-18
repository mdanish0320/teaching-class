from rest_framework import serializers
from .models import Product, Category, Supplier
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"  # This will include all fields from the Category model


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"  # This will include all fields from the Supplier model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # This will include all fields from the Supplier model


class ProductSerializer(serializers.ModelSerializer):
    # name must match with the models
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    # name must match with the input json
    # category_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(), write_only=True
    # )
    # supplier_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Supplier.objects.all(),
    #     many=True,
    #     allow_empty=False,  # Do not allow empty arrays
    #     write_only=True,
    # )

    # category_id = serializers.IntegerField(write_only=True)
    # supplier_id = serializers.IntegerField(write_only=True)

    # # Making the 'user' field optional in the serializer
    # user = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(), allow_null=True, required=False
    # )

    class Meta:
        model = Product
        fields = "__all__"  # This will include all fields from the Product model
        # fields = [
        #     "id",
        #     "category",
        #     "supplier",
        #     "name",
        #     "description",
        #     "price",
        #     "category_id",
        #     "supplier_id",
        # ]

    # def create(self, validated_data):

    #     supplier = validated_data.pop("supplier_id")
    #     category = validated_data.pop("category_id")

    #     product = Product.objects.create(category=category, **validated_data)
    #     product.supplier.set(supplier)
    #     return product

from rest_framework import serializers
from .models import Category, Supplier, Product

# class CategorySerialzer(serializers.Serializer):


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SupplierSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductSerialzer(serializers.ModelSerializer):
    category = CategorySerialzer(read_only=True)
    supplier = SupplierSerialzer(many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), many=True, write_only=True, allow_empty=False
    )

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        category_obj = validated_data.pop("category_id")
        supplier_obj = validated_data.pop("supplier_id")

        product = Product.objects.create(**validated_data, category=category_obj)
        product.supplier.set(supplier_obj)

        serialzier = ProductSerialzer(product)

        return serialzier.data

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

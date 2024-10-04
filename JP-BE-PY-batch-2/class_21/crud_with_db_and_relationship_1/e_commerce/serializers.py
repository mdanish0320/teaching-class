from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    status = serializers.IntegerField(write_only=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)    


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    category_id = serializers.IntegerField(write_only=True)  # Nested serializer for category
    categories = CategorySerializer(read_only=True, source='category')  # Nested serializer for category
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)  

# REVERSE DATA POPULATION

class ProductReverseCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)         


class CategoryReverseProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    status = serializers.IntegerField(write_only=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)       
    
    products = ProductReverseCategorySerializer(many=True, read_only=True, source='category')  # source='category' is the related_name




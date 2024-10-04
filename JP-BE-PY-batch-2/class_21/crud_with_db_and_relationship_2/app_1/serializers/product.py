from rest_framework import serializers

from .category import CategorySerializer

class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    
    category = CategorySerializer(read_only=True, many=True)
    category_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )


class ProductCategorySerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    category_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )    

    # def validate_category_ids(self, ids):
    #     print("validate_category_ids", ids)
    #     from app_1.models.category import Category as category_model
    #     db_categories = category_model.objects.filter(id__in=ids).all()
    #     if len(db_categories) != len(ids):
    #         raise serializers.ValidationError("One or more category IDs are invalid.")
    #     return ids
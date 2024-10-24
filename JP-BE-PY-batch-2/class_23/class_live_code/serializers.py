from rest_framework import serializers
from .models import Category, Supplier, Product

# class CategorySerialzer(serializers.Serializer):

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        # fields = ['name', 'description']


class SupplierSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        # fields = ['name', 'description']        


class ProductSerialzer(serializers.ModelSerializer):
    category = CategorySerialzer(read_only=True)
    supplier = SupplierSerialzer(many=True, read_only=True)

    # category_id = serializers.IntegerField(write_only=True) 
    # supplier_id = serializers.ListField(write_only=True) 

    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), many=True, write_only=True)
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ['name', 'description']   
        # 

    def create(self, validated_data):
        print("serializer create")
        category_obj = validated_data.pop("category_id")
        supplier_obj = validated_data.pop("supplier_id")

        print("validated_dataa", validated_data, category_obj)

        # category_obj = Category.objects.filter(id=category_obj).first()
        # if category_obj is None:
        #     raise serializers.ValidationError("category not found")
        # supplier_obj = Supplier.objects.filter(id__in=supplier_obj)

        product = Product.objects.create(**validated_data, category=category_obj)
        product.supplier.set(supplier_obj)

        serialzier = ProductSerialzer(product)

        return serialzier.data
        # return super().perform_create(serializer)



proudcts = proudct.objhects.all()        

for product in products:
    category = Category.objects.filter(id=proudct.category.id).first()

    merge(proudct, category)
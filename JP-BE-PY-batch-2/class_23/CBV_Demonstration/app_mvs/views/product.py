from rest_framework.viewsets import ModelViewSet
from app_mvs.models import Product
from app_mvs.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)


class CustomPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = "page_size"
    max_page_size = 100  # Maximum page size


class ProductViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: ProductSerializer):
        # Get validated data
        validated_data = serializer.validated_data

        # Extract supplier and category from validated data
        supplier = validated_data.pop("supplier")  # Use the correct field name
        category = validated_data.pop("category")  # Use the correct field name

        # Create the product instance
        product: Product = serializer.save(category=category, user=self.request.user)
        # product = Product.objects.create(
        #     category=category, **validated_data, user=self.request.user
        # )

        # Set the suppliers for the product
        product.supplier.set(supplier)  # Assuming supplier is a list of IDs

        # Optionally return the product or you can just let it save automatically
        return product

    def get_serializer_class(self):
        return super().get_serializer_class()

    # in modelviewset, this is class scope method.
    # it will run on every http methods even in single object api like get, put, delete etc
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    # in modelviewset, this is class scope method.
    # it will run on every http methods even in single object api like get, put, delete etc
    def filter_queryset(self, queryset):
        filter_queryset = super().filter_queryset(queryset)
        input = self.request.query_params
        if input.get("id") is not None:
            filter_queryset = filter_queryset.filter(category__id=input.get("id"))
        return filter_queryset

    # this will only run in single object API i.e put, delete, patch and get with id
    def get_object(self):
        result = super().get_object()
        if result.user_id == 2:
            raise PermissionDenied("You do not have permission to access this product.")

        return result

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.user.is_superuser:
            return [IsAuthenticated(), IsAdminUser()]
        return permissions

    def get_pagination_class(self):
        # You can conditionally return different pagination classes based on the request
        if self.request.query_params.get("pagination_type") == "limit_offset":
            return LimitOffsetPagination
        elif self.request.query_params.get("pagination_type") == "cursor":
            return CursorPagination
        else:
            return CustomPagination  # Default pagination class

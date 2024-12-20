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
from rest_framework.decorators import action
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = "page_size"
    max_page_size = 100  # Maximum page size


class ProductViewSet(ModelViewSet):
    queryset = (
        Product.objects.all()
    )
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    # http://localhost:8000/app_mvs/products/recent/
    @action(detail=False, methods=["get"])
    def recent(self, request):
        recent_products = Product.objects.filter(price__gte=200)
        serializer = self.get_serializer(recent_products, many=True)
        return Response(serializer.data)

    # http://localhost:8000/app_mvs/products/2/special/
    @action(detail=True, methods=["get"])
    def special(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    def perform_create(self, serializer: ProductSerializer):
        # Get validated data
        validated_data = serializer.validated_data

        # Extract supplier and category from validated data
        supplier = validated_data.pop("supplier_id")  # Use the correct field name
        category = validated_data.pop("category_id")  # Use the correct field name

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
    # def filter_queryset(self, queryset):
    #     filter_queryset = super().filter_queryset(queryset)
    #     input = self.request.query_params
    #     if input.get("id") is not None:
    #         filter_queryset = filter_queryset.filter(category__id=input.get("id"))
    #     return filter_queryset

    # this will only run in single object API i.e put, delete, patch and get with id
    # def get_object(self):
    #     result = super().get_object()
    #     if result.user_id == 2:
    #         raise PermissionDenied("You do not have permission to access this product.")

    #     return result

    # def get_permissions(self):
    #     permissions = super().get_permissions()
    #     if self.request.user.is_superuser:
    #         return [IsAuthenticated(), IsAdminUser()]
    #     return permissions

    def get_pagination_class(self):
        # You can conditionally return different pagination classes based on the request
        if self.request.query_params.get("pagination_type") == "limit_offset":
            return LimitOffsetPagination
        elif self.request.query_params.get("pagination_type") == "cursor":
            return CursorPagination
        else:
            return CustomPagination  # Default pagination class

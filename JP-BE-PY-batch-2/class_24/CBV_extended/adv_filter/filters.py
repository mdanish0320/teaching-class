from django_filters import rest_framework as filters
from django.db.models import Q

from app.models import Product


class ProductFilter(filters.FilterSet):
    supplier_id = filters.NumberFilter(field_name="supplier__id")
    supplier_name = filters.CharFilter(
        field_name="supplier__name", lookup_expr="icontains"
    )
    category_id = filters.NumberFilter(field_name="category__id")
    category_name = filters.CharFilter(
        field_name="category__name", lookup_expr="icontains"
    )
    name = filters.CharFilter(field_name="name", lookup_expr="exact")
    name_like = filters.CharFilter(field_name="name", lookup_expr="icontains")
    name_start = filters.CharFilter(field_name="name", lookup_expr="istartswith")
    price_gt = filters.NumberFilter(field_name="price", lookup_expr="gt")
    price_lt = filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Product
        fields = [
            "supplier_id",
            "supplier_name",
            "category_id",
            "category_name",
            "name",
            "name_like",
            "name_start",
            "price_gt",
            "price_lt",
        ]

    # def filter_search(self, queryset, name, value):
    #     """
    #     Filter the queryset to include products that match the search term in the Supplier name,
    #     Category name, or Product name.
    #     """
    #     if value:
    #         # Construct a Q object to filter based on the search term
    #         query = (
    #             Q(name__icontains=value)
    #             | Q(supplier__name__icontains=value)
    #             | Q(category__name__icontains=value)
    #         )
    #         return queryset.filter(query)
    #     return queryset

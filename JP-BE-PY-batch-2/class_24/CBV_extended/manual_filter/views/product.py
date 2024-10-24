from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerialzer


# Create your views here.
class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerialzer

    def filter_queryset(self, queryset):
        filter_queryset = super().filter_queryset(queryset)
        qp = self.request.query_params

        if qp.get("supplier_id") is not None:
            filter_queryset = filter_queryset.filter(supplier__id=qp.get("supplier_id"))

        if qp.get("supplier_name") is not None:
            filter_queryset = filter_queryset.filter(
                supplier__name=qp.get("supplier_name")
            )

        if qp.get("category_id") is not None:
            filter_queryset = filter_queryset.filter(category__id=qp.get("category_id"))

        if qp.get("category_name") is not None:
            filter_queryset = filter_queryset.filter(
                category__name=qp.get("category_name")
            )

        if qp.get("name") is not None:
            filter_queryset = filter_queryset.filter(name=qp.get("name"))

        if qp.get("name_like") is not None:
            filter_queryset = filter_queryset.filter(
                name__icontains=qp.get("name_like")
            )

        if qp.get("name_start") is not None:
            filter_queryset = filter_queryset.filter(
                name__istartswith=qp.get("name_start")
            )

        if qp.get("price_gt") is not None:
            filter_queryset = filter_queryset.filter(price__gt=qp.get("price_gt"))

        if qp.get("price_lt") is not None:
            filter_queryset = filter_queryset.filter(price__lt=qp.get("price_lt"))

        return filter_queryset

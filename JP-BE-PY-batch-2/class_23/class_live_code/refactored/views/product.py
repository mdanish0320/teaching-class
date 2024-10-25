from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerialzer


# Create your views here.
class ProductModelViewSet(ModelViewSet):
    queryset = (
        Product.objects.select_related("category").prefetch_related("supplier").all()
    )
    serializer_class = ProductSerialzer

    # for put and patch methods
    # we would have different input

    # def get_serializer_class(self):
    #     if self.request.method == "POST":
    #         return MyModelCreateSerializer
    #     elif self.request.method == "PUT":
    #         return MyModelUpdateSerializer
    #     elif self.request.method == "PATCH":
    #         return MyModelPartialUpdateSerializer
    #     return super().get_serializer_class()  # Fallback to the default serializer

    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)

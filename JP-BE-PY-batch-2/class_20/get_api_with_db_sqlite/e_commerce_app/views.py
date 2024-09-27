from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product

@api_view(['GET'])
def get_all_products(request):
    # Use Django's serialize function to convert queryset to JSON format
    products = Product.objects.all()

    # Manually build the list of dictionaries representing each product
    product_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'cat_id': product.cat_id,
            'created_at': product.created_at
        }
        product_list.append(product_data)

    return Response(product_list)
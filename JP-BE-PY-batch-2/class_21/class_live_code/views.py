from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Category as category_model, Product as product_model
from .models import Categoryy as category_model_2, Productt as product_model_2

from .serializers import CategorySerializer, ProductSerializer
from .serializers import CategoryySerializer, ProducttSerializer



@api_view(['GET', 'POST'])
def get_categories_or_create_category(requst: Request):
    data = []
    if requst.method == 'GET':
        params = requst.query_params
        
        category_objects = category_model.objects
        if params.get("name") is not None:
            category_objects = category_objects.filter(name=params.get("name"))

        if params.get("id") is not None:
            category_objects = category_objects.filter(id=params.get("id"))

        categories = category_objects.all()
        # for category in categories:
        #     data.append({
        #         "id": category.id,
        #         "user_id": category.user_id,
        #         "name": category.name,
        #         "created_at": category.created_at,
        #         "updated_at": category.updated_at
        #     })
        serializer = CategorySerializer(categories, many=True)
        data = serializer.data
    
    if requst.method == 'POST':
        # name = data.get("name")

        # if type(name) is not str or len(name) == 0 or len(name.strip()) == 0:
        #     return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)

        
        serializer = CategorySerializer(data=requst.data)
        print("before is_valid", serializer.initial_data)
        if serializer.is_valid():
            print("after is_valid", serializer.validated_data)
            category_model.objects.create(**serializer.validated_data)
        else:
            return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        data = "success"

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_category(requst: Request, id):
    data = {}
    category = category_model.objects.get(pk=id)
    if requst.method == 'GET':
        data = {
                "id": category.id,
                "name": category.name,
                "created_at": category.created_at,
                "updated_at": category.updated_at
            }
    
    if requst.method == 'PUT':
        data = requst.data
        name = data.get("name")
        category.name = name
        category.save()

        data = {
                "id": category.id,
                "name": category.name,
                "created_at": category.created_at,
                "updated_at": category.updated_at
            }


    if requst.method == 'DELETE':
        category.delete()
        data = "deleted"

    return Response(data, status=status.HTTP_200_OK)





@api_view(['GET', 'POST'])
def create_or_get_products(requst: Request):
    data = []
    if requst.method == 'GET':
        product = product_model.objects.select_related("category").all()
        print("after product query")
        serializer = ProductSerializer(product, many=True)

        print("after serialzer.data")
        data = serializer.data
        print("dadsfsdfsdaf")


        return Response(data, status=status.HTTP_200_OK)
    
    if requst.method == 'POST':
        serializer = ProductSerializer(data=requst.data)
        if serializer.is_valid():
            category_id = serializer.validated_data['category_id']
            category = category_model.objects.filter(id=category_id).first()
            if category is None:
                return Response("invalid category", status=status.HTTP_400_BAD_REQUEST)
            product_model.objects.create(**serializer.validated_data)
        else:
            return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        data = "success"

    return Response(data, status=status.HTTP_201_CREATED)


# data = []
# proudcts = product_model.objects.all() #
# for product in proudcts:
#     categorie = category_model.objects.filter(id=product.category_id).first()
#     data.append(
#         **product,
#         "category": **category
#     )

# return data



@api_view(['GET', 'POST'])
def create_or_get_categories_2(requst: Request):
    data = []
    if requst.method == 'GET':
        category = category_model_2.objects.all()
        serializer = CategoryySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if requst.method == 'POST':
        serializer = CategoryySerializer(data=requst.data)
        if serializer.is_valid():
            category_model_2.objects.create(**serializer.validated_data)
        else:
            return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        data = "success"

    return Response(data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'POST'])
def create_or_get_products_2(requst: Request):
    data = []
    if requst.method == 'GET':
        product = product_model_2.objects.prefetch_related("category").all()
        serializer = ProducttSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if requst.method == 'POST':
        serializer = ProducttSerializer(data=requst.data) # {"name": "prod", "category_id": 1}
        if serializer.is_valid():
            category_id = serializer.validated_data.pop("category_id")
            product = product_model_2.objects.create(**serializer.validated_data)
            product.category.set(category_id)
            # product_model_2.objects.create(name="product 1", category_id="cate")
        else:
            return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        data = "success"

    return Response(data, status=status.HTTP_201_CREATED)
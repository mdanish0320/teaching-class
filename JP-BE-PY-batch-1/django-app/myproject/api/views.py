from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializers

@api_view(['GET'])
def getData(request):
    person = {"name": "danish"}
    return Response(person)


# @api_view(['POST'])
# def getData(request):
#     person = {"name": "danish"}
#     return Response(person)


@api_view(['GET'])
def get_db(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from .models import category as category_model
from .serializers import CategorySerializer


class CategoryCreateListAPIView(APIView):
    # authentication_classes = []
    # permission_classes = []

    def get(self, request):
        params = self.request.query_params

        category_objects = category_model.objects
        if params.get("name") is not None:
            category_objects = category_objects.filter(name=params.get("name"))

        if params.get("id") is not None:
            category_objects = category_objects.filter(id=params.get("id"))

        categories = category_objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = CategorySerializer(data=self.request.data)
        print("Before serialization:", serializer.initial_data)
        if serializer.is_valid():
            print("after validation:", serializer.validated_data)
            category_model.objects.create(**serializer.validated_data)

            return Response("success", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryRetriveUpdateDestroy(APIView):
    def get(self, request, pk):
        category = category_model.objects.get(pk=pk)

        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = category_model.objects.get(pk=pk)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            # Loop through all fields in validated_data and update the instance
            for key, value in serializer.validated_data.items():
                setattr(category, key, value)
            category.save()
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = category_model.objects.get(pk=pk)
        category.delete()
        return Response("deleted", status=status.HTTP_200_OK)

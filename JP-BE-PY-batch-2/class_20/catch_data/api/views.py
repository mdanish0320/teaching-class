from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

@api_view(['GET', 'POST'])
def query_params_example(request: Request):
    if request.method == 'GET':
        # Access query parameters
        param1 = request.query_params.get('param1')  # Example: /api/persons/?param1=value
        param2 = request.query_params.get('param2')  # Example: /api/persons/?param2=value
    
        return Response({'param1': param1, 'param2': param2}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Access JSON input
        data = request.data  # Data will contain parsed JSON
        value1 = data.get('key1')
        value2 = data.get('key2')
        
        return Response({'key1': value1, 'key2': value2}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def path_params_example(request, id):
    # `id` is captured from the URL pattern
    return Response({'id': id}, status=status.HTTP_200_OK)

    


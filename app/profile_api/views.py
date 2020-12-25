from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets

# APIView
class HelloApiView(APIView):
    '''Testing api view'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''RETURNS a list of APIVIEW'''
        an_apiview = [
            'Uses Http methods',
            'is similar to a tradition',
            'hello world',
            'its mapped to urls',
        ]

        return Response({
            'messages': 'hello!',
            'api view': an_apiview
        })

    def post(self, request):
        '''Creates a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({
                'message': message
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''update whole object using put request'''
        return Response({'method': 'Is a put request'})

# Viewset
class HelloViewSet(viewsets.ViewSet):
    '''Testing viewset api'''
    def list(self, request):
        '''get a list from api'''
        a_viewset = [
            'uses some actions',
            'it is very good',
            'it is very awful',
        ]

        return Response({
            'message': 'hello world',
            'a_viewset': a_viewset
        })
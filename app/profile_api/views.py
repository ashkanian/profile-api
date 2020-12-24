from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    '''Testing api view'''

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

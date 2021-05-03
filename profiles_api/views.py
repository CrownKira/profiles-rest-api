from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    # define app logic for our endpoint
    # that we are going to assign to this view

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        # to retrieve a list of objects, or a specific object
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to the URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

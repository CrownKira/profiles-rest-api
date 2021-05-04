from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters # add filter to viewset
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    # define app logic for our endpoint
    # that we are going to assign to this view
    serializer_class = serializers.HelloSerializer

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

    def post(self, request):
        """Create a hello message with our name"""
        # serializer_class method is a method of parent class (in ApiView)
        serializer = self.serializer_class(data=request.data)

        # validate a serializer
        if serializer.is_valid():
            # retrieve the name field
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST,
                )

    def put(self, request, pk=None):
        # pk is at the back of the url
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    # need to point to model
    # for model view set, assign these two, django will take care of 
    # modifying operation for us 
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # can config one or more types, just add to this classes
    authentication_classes = (TokenAuthentication,)
    # DRF does all these for us, we just need to assign
    permission_classes = (permissions.UpdateOwnProfile,)
    # filter these fields using this filter backend
    # use search param to get the items (eg. ?search=Test)
    filter_backends = (filters.SearchFilter,)
    # allows to search for this viewset by name or email field
    # adding this assignment will add to the routers the 
    # url pattern matching that detects search param
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    # make it visible to the browsable api
    # add to obtain auth token 
    # enable in django admin
    # render this in browsable api
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


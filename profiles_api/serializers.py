from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
  """Serializes a name field for testing our APIView"""
  # make sure the content is of the correct type
  name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
  """Serializes a user profile object"""
  # config the meta nested class to make 
  # the serializer point to a specific model in our project
  class Meta:
    model = models.UserProfile
    # list of fields we want to work with 
    fields = ('id', 'email', 'name', 'password')
    # custom config for the following fields
    # write_only: can only use it to create new obj, etc
    # cant use it to retrieve object
    # custom style: only for browsable api
    extra_kwargs = {
      'password': {
        'write_only': True,
        'style': {'input_type': 'password'}
      }
    }

  def create(self, validated_data): 
    """Create and return a new user"""
    # so that the password created as a hash 
    # not the clear text password
    # override the create function 
    # call the create_user function
    # defined in UserProfileManager
    user = models.UserProfile.objects.create_user(
      email=validated_data['email'],
      name=validated_data['name'],
      password=validated_data['password']
    )

    return user

  def update(self, instance, validated_data):
    """Handle updating user account"""
    # password requires some additional logic 
    # to hash the password before saving the update 
    # don't store the password in clear text 
    if 'password' in validated_data:
      password = validated_data.pop('password')
      instance.set_password(password)
    
    # let the parent update handle the remaining data
    return super().update(instance, validated_data)
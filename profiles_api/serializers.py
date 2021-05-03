from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
  """Serializes a name field for testing our APIView"""
  # make sure the content is of the correct type
  name = serializers.CharField(max_length=10)
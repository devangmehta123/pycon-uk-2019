from rest_framework import serializers
from .fields import PostcodeField

class SimplePostcodeRequestSerializer(serializers.Serializer):
    postcode = PostcodeField()


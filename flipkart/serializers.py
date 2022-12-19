from django.urls import path, include

from rest_framework import routers, serializers, viewsets
from .models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = registration
        fields = '__all__'
        


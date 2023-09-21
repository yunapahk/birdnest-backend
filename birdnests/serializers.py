from rest_framework import serializers
from .models import Birdnest

class BirdnestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birdnest
        fields = ['id', 'name', 'category', 'description']

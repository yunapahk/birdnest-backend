from .models import Birdnest
from rest_framework import viewsets
from .serializers import BirdnestSerializer

class BirdnestViewSet(viewsets.ModelViewSet):
    queryset = Birdnest.objects.all()
    serializer_class = BirdnestSerializer

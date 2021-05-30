from rest_framework import viewsets

from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

from rest_framework import generics
from .serializers import PlaceSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Place

class PlaceList(generics.ListAPIView):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer
  permission_classes = IsAuthenticated,

class PlaceDetail():
  pass


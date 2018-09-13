from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.serializers import DishSerializer
from dcxt.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Dishs to be viewed or edited.
    """
    queryset = Dish.objects.all().order_by('weight')
    serializer_class = DishSerializer
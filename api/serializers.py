from rest_framework import serializers
from dcxt.models import Dish


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('name','price','discount_price','discount','pictures','weight','introduction')

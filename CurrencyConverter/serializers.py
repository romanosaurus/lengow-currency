from CurrencyConverter.models import Cube
from rest_framework import serializers


class ConversionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cube
        fields = ['answer']
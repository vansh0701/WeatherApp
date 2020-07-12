from rest_framework import serializers
from .models import WeatherData

class EmbededSerializer(serializers.ModelSerializer):
    class Meta:
        model=WeatherData
        fields='__all__'
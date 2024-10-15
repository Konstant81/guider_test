from rest_framework import serializers
from .models import City, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    streets = serializers.StringRelatedField(many=True)
    class Meta:
        model= City
        fields = ['streets']

class ShopListSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    street = serializers.StringRelatedField()
    
    class Meta:
        model= Shop
        fields = '__all__'

class ShopCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Shop
        fields = '__all__'

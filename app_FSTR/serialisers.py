from .models import User, Mountain, Coordinates, Level, Images
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'second_name', 'last_name', 'phone', 'email']


class CoordinatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['mountain', 'created', 'title']


class MountainSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    coordinates = CoordinatesSerializer(read_only=True)
    levels = LevelSerializer(read_only=True)
    images = ImagesSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Mountain
        fields = ['user', 'created', 'title', 'other_titles', 'coordinates', 'levels', 'status']

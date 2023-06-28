from .models import *
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
        fields = ['title', 'created', 'image']


class MountainSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coordinates = CoordinatesSerializer()
    levels = LevelSerializer()

    class Meta:
        model = Mountain
        fields = [
            'id', 'user', 'levels', 'coordinates', 'add_time', 'status', 'beauty_title', 'connect', 'title',
            'other_titles'
        ]

    def create(self, validated_data):
        print(validated_data)
        thing_data_1 = validated_data.pop('user')
        thing_data_2 = validated_data.pop('levels')
        thing_data_3 = validated_data.pop('coordinates')
        user_serializer = UserSerializer(data=thing_data_1)
        level_serializer = LevelSerializer(data=thing_data_2)
        coord_serializer = CoordinatesSerializer(data=thing_data_3)
        user_serializer.is_valid(raise_exception=True)
        level_serializer.is_valid(raise_exception=True)
        coord_serializer.is_valid(raise_exception=True)
        validated_data['user'] = user_serializer.save()
        validated_data['levels'] = level_serializer.save()
        validated_data['coordinates'] = coord_serializer.save()
        instance = super().create(validated_data)
        return instance


class MountainUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mountain
        fields = [
            'add_time', 'beauty_title', 'connect', 'title', 'other_titles'
        ]













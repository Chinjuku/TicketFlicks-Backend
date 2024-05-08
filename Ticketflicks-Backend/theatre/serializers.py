from rest_framework import serializers
from .models import Theatre, Place

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ['id', 'theatre_num', 'show_time']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    theatre = TheatreSerializer(many=False)
    class Meta:
        model = Place
        fields = ['seat_num', 'theatre']

    
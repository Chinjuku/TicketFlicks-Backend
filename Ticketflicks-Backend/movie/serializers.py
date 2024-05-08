from rest_framework import serializers
from .models import Movie, Actor, Category
from theatre.serializers import TheatreSerializer

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    actors = ActorSerializer(many=True)
    theatre = TheatreSerializer(many=False)
    movie_img = serializers.ImageField(required=False)

    class Meta:
        model = Movie
        fields = '__all__'

from rest_framework import serializers
from .models import Movie, Actor, Category

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        models = Actor
        fields = [ 'actor_name' ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = [ 'category_name' ]
from rest_framework import serializers
from .models import Movie, Actor, Category, IPAddress
from theatre.serializers import TheatreSerializer

class IPAddressSerializer(serializers.Serializer):
    class Meta:
        model = IPAddress
        fields = '__all__'

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
    movie_img_url = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_movie_img_url(self, obj):
        if obj.movie_img:
            return obj.movie_img.url
        return None

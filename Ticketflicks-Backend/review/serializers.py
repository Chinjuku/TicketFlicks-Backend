from movie.serializers import MovieSerializer
from rest_framework import serializers
from .models import Reply, Review
from useraccount.serializers import UserDetailSerializer

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=False)
    movie = MovieSerializer(many=False)
    class Meta:
        model = Review
        fields = '__all__'

class ReviewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CountReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('movie','count_review')


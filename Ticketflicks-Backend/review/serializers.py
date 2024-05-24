from rest_framework import serializers
from .models import Reply, Review

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CountReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('movie','count_review')


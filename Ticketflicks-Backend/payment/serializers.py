from rest_framework import serializers
from .models import Payment
from theatre.serializers import PlaceSerializer

class PaymentSerializer(serializers.ModelSerializer):
    seats = PlaceSerializer(many=True)

    class Meta:
        model = Payment
        fields = '__all__'
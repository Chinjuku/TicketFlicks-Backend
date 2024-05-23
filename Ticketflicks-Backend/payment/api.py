import json
from datetime import datetime, timedelta
from .models import Payment
from theatre.models import Place
from theatre.serializers import PlaceSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import PaymentSerializer

@csrf_exempt
def payment(request):
    # http://localhost:8000/api/payment/
    data = json.loads(request.body)
    if request.method == 'POST':
        try:
            seats = data.get('ticket_seats', [])
            places = Place.objects.filter(id__in=seats)
            payment = Payment.objects.create(
                payment_id=data['payment_id'],
                client_secret=data['client_secret'],
                payment_method=data['payment_method'],
                amounts=data['amounts']
            )
            payment.seats.set(places)
            payment.save()
            serializer = PaymentSerializer(payment)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    if request.method == 'GET':
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_payment(request, pk):
    if request.method == 'GET':
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment, many=False)
        return JsonResponse(serializer.data, safe=False)
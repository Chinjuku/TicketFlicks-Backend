import json

from movie.models import Movie
from .models import Theatre, Place
from .serializers import TheatreSerializer, PlaceSerializer, SeatSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

@csrf_exempt
def theatre(request, pk):
    # http://localhost:8000/api/theatre/uuid
    if request.method == 'GET':
        theatre = Theatre.objects.get(pk=pk)
        serializer = TheatreSerializer(theatre, many=False)
        return JsonResponse(serializer.data, safe=False)

# Select Theatre + Time to show
@csrf_exempt
def place(request, pk):
    # http://localhost:8000/api/place/uuid
    if request.method == 'GET':
        place = Place.objects.filter(theatre=pk)
        serializer = PlaceSerializer(place, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def select_place(request):
    # send form -> {
        # "seat" : [ "id1", "id2" ]
    # }
    if request.method == 'GET':
        try:
            data = json.loads(request.body)
            ids = data.get('seats', [])  # Get list of IDs from request body
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        # Filter places based on the list of IDs
        places = Place.objects.filter(id__in=ids)
        serializer = SeatSerializer(places, many=True)
        theatre_id = places.first().theatre.id
        # Find price from Movie
        movie = Movie.objects.filter(theatre=theatre_id).first()
        # Count places
        price = movie.price
        vip_price = places.filter(type="vip").count() * price
        countnormal = places.filter(type="normal").count() * price
        countvip =  vip_price * 0.07 + vip_price
        # Serialize filtered places       
        response_data = {
            "seats": serializer.data,
            "allprice": countnormal + countvip
        }
        return JsonResponse(response_data, safe=False)

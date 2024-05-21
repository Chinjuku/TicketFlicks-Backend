import json
from datetime import datetime, timedelta
from movie.models import Movie
from .models import Theatre, Place
from .serializers import TheatreSerializer, PlaceSerializer, SeatSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def theatre(request, pk):
    # http://localhost:8000/api/theatre/uuid/
    # Load data from json
    data = json.loads(request.body)
    theatre_num = int(data.get('theatre_num'))
    show_time = data.get('show_time')
    if request.method == 'GET':
        theatre = Theatre.objects.get(pk=pk)
        serializer = TheatreSerializer(theatre, many=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        Theatre.objects.filter(pk=pk).update(theatre_num=theatre_num, show_time=show_time)
        return JsonResponse({'message': 'Theatre updated successfully'}, status=200)
    elif request.method == 'DELETE':
        theatre = Theatre.objects.get(pk=pk)
        theatre.delete()
        return JsonResponse({'message': 'Theatre deleted successfully'}, status=200)
    return JsonResponse({'error': 'Theatre Error'})

@csrf_exempt
def all_theatre(request, movieId, date):
    now = datetime.today() - timedelta(hours=2)
    wantdate = datetime.strptime(date, '%Y-%m-%d').date()
    # http://localhost:8000/api/alltheatre/movieId/date/
    if request.method == 'GET':
        theatre = Theatre.objects.filter(movie=movieId, show_time__date=wantdate).order_by('show_time')
        serializer = TheatreSerializer(theatre, many=True)
        theatre_data = serializer.data
        grouped_data = {}
        for item in theatre_data:
            theatre_num = item['theatre_num']
            if theatre_num not in grouped_data:
                grouped_data[theatre_num] = []
            grouped_data[theatre_num].append(item)
        return JsonResponse(grouped_data, safe=False)
    if request.method == 'PUT':
        Theatre.objects.filter(show_time=now).update(is_show=False)
        return JsonResponse({ 'message': now }, safe=False)

@csrf_exempt
def create_theatre(request):
    # http://localhost:8000/api/createtheatre/
    data = json.loads(request.body)
    if request.method == 'POST':
        serializer = TheatreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

# Select Theatre + Time to show
@csrf_exempt
def place(request, pk):
    # http://localhost:8000/api/place/
    if request.method == 'GET':
        place = Place.objects.filter(theatre=pk)
        serializer = PlaceSerializer(place, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def select_place(request):
    # send form -> {
        # "seat" : [ "id1", "id2" ]
    # }
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ids = data.get('seats', [])  # Get list of IDs from request body
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        # Filter places based on the list of IDs
        places = Place.objects.filter(id__in=ids)
        serializer = SeatSerializer(places, many=True)
        movie_id = places.first().theatre.movie.id
        movie = Movie.objects.get(id=movie_id)
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

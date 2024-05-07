from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import Movie
from ..serializers import MovieSerializer
from datetime import date, timedelta

today = date.today()
future4days = today + timedelta(days=4)
future7days = today + timedelta(days=7)

@csrf_exempt
def all_movie(request):
    """List all code snippets, or create a new snippet."""
    if request.method == 'GET':
        movies = Movie.objects.all().select_related('theatre').prefetch_related('actors', 'categories')
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = MovieSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def select_movie(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, many=False)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def recommand_movie(request):
    if request.method == 'GET':
        movie = Movie.objects.filter(rating__gte=9)
        serializer = MovieSerializer(movie, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def onshow_movie(request):
    if request.method == 'GET':
        movie = Movie.objects.filter(showing_date__gte=future4days, showing_due__lte=today)
        serializer = MovieSerializer(movie, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def comming_movie(request):
    if request.method == 'GET':
        movie = Movie.objects.filter(showing_date__gt=future7days)
        serializer = MovieSerializer(movie, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def favorite_movie(request):
    if request.method == 'GET':
        movie = Movie.objects.filter(favorite=True)
        serializer = MovieSerializer(movie, many=True)
        return JsonResponse(serializer.data, safe=False)
    


    


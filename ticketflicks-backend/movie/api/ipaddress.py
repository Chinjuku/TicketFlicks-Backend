import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..serializers import MovieSerializer
from ..models import IPAddress, Movie

@csrf_exempt
def all_fav(request, movieId):
    client_ip = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        # Get client's IP address
        movie = Movie.objects.get(pk=movieId)
        ip_movieId_exists = IPAddress.objects.filter(ip=client_ip, movieId=movieId).exists()
        if not ip_movieId_exists:
            ip_object = IPAddress.objects.create(ip=client_ip, movieId=movie, favorite=True)
        else:
            ip_object = IPAddress.objects.get(ip=client_ip, movieId=movie)
            ip_object.favorite = not ip_object.favorite
            ip_object.save()
        return JsonResponse({"message": ip_object.favorite}, safe=False)
    elif request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=movieId)
        except Movie.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)
        movies_with_favorite_ip = Movie.objects.get()
        serializer = MovieSerializer(movies_with_favorite_ip, many=False)
        return JsonResponse(serializer.data, safe=False)
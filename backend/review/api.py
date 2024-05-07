from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import ReplySerializer, ReviewSerializer
from .models import Review

@csrf_exempt
def review(request, movieId):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movieId)
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer, safe=False)
    
@csrf_exempt
def reply(request, reviewId):
    if request.method == 'GET':
        reply = Review.objects.filter(review_id=reviewId)
        serializer = ReplySerializer(reply, many=False)
        return JsonResponse(serializer, safe=False)
        
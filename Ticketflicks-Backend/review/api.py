from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializers import ReplySerializer, ReviewSerializer
from .models import Review
import json

@csrf_exempt
def review(request, movieId):
    data = json.loads(request.body)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movieId)
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False), HttpResponse(status=status.HTTP_201_CREATED)

@csrf_exempt
def update_del_review(request, reviewId):
    data = json.loads(request.body)
    name = data.get('name')
    review_comment = data.get('review_comment')
    stars = data.get('stars')
    if request.method == 'PUT':
        Review.objects.filter(pk=reviewId).update(name=name, stars=stars, review_comment=review_comment)
        return JsonResponse({"message": "update successfully"}, safe=False)
    elif request.method == 'DELETE':
        Review.objects.filter(pk=reviewId).delete()
        return JsonResponse({"message": "delete successfully"}, safe=False)
    
@csrf_exempt
def reply(request, reviewId):
    data = json.loads(request.body)
    if request.method == 'GET':
        reply = Review.objects.filter(review_id=reviewId)
        serializer = ReplySerializer(reply, many=False)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = ReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def update_del_reply(request, replyId):
    data = json.loads(request.body)
    name = data.get('name')
    reply_comment = data.get('reply_comment')
    if request.method == 'PUT':
        Review.objects.filter(pk=replyId).update(name=name, reply_comment=reply_comment)
        return JsonResponse({"message": "update successfully"}, safe=False)
    elif request.method == 'DELETE':
        Review.objects.filter(pk=replyId).delete()
        return JsonResponse({"message": "delete successfully"}, safe=False)
    
        
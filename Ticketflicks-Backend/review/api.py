from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from movie.models import Movie
from movie.serializers import MovieSerializer
from rest_framework import status
from .serializers import CountReviewSerializer, ReplySerializer, ReviewPostSerializer, ReviewSerializer
from .models import Reply, Review
import json
from django.db.models import Count

# Review

@csrf_exempt
def count_review(request):
    if request.method == 'GET':
        reviews = Review.objects.values("movie").annotate(count_review=Count("movie"))
        review_data = list(reviews)
        return JsonResponse(review_data, safe=False)

@csrf_exempt
def count_review_id(request, movieId):
    if request.method == "GET":
        try:
            count_review = Review.objects.filter(movie=movieId).count()
            return JsonResponse(count_review, safe=False)
        except Exception as e:
            return JsonResponse({"error" : str(e)}, safe=False)

@csrf_exempt
def count_reply_id(request):
    if request.method == "GET":
        try:
            count_reply = Reply.objects.values("review_id").annotate(count_reply=Count("review_id"))
            reply_data = list(count_reply)
            return JsonResponse(reply_data, safe=False)
        except Exception as e:
            return JsonResponse({"error" : str(e)}, safe=False)

@csrf_exempt
def all_review_movie(request, movieId):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movieId)
        reviews = Review.objects.filter(movie=movie).order_by('-time_stamp')
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def review(request, reviewId):
    if request.method == 'GET':
        try:
            review = Review.objects.get(pk=reviewId)
            serializer = ReviewSerializer(review, many=False)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, safe=False)

@csrf_exempt
def post_review(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = ReviewPostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)  # Use status 201 for successful creation
            else:
                return JsonResponse(serializer.errors, status=400)  # Return validation errors
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  # Return generic server error

    

@csrf_exempt
def update_del_review(request, reviewId):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            review_comment = data.get('review_comment')
            stars = data.get('stars')
            Review.objects.filter(pk=reviewId).update(name=name, stars=stars, review_comment=review_comment)
            return JsonResponse({"message": "update successfully"}, safe=False)
        except Exception as e:
            print(str(e))
            return JsonResponse({"error": str(e)}, status=500)
    elif request.method == 'DELETE':
        Review.objects.filter(pk=reviewId).delete()
        return JsonResponse({"message": "delete successfully"}, safe=False)

# Reply
@csrf_exempt
def reply(request):
    if request.method == 'GET':
        try:
            reply = Reply.objects.all().order_by('-time_stamp')
            serializer = ReplySerializer(reply, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = ReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_reply_by_id(request, replyId):
    if request.method == 'GET':
        reply = Reply.objects.get(id=replyId)
        serializer = ReplySerializer(reply, many=False)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def update_del_reply(request, replyId):
    if request.method == 'PUT':
        data = json.loads(request.body)
        name = data.get('name')
        reply_comment = data.get('reply_comment')
        Reply.objects.filter(pk=replyId).update(name=name, reply_comment=reply_comment)
        return JsonResponse({"message": "update successfully"}, safe=False)
    elif request.method == 'DELETE':
        Reply.objects.filter(pk=replyId).delete()
        return JsonResponse({"message": "delete successfully"}, safe=False)
    
        
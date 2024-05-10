import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..serializers import CategorySerializer
from ..models import Category

@csrf_exempt
def all_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)
    
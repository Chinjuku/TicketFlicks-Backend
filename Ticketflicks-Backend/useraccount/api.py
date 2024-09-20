from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import User
from .serializers import UserDetailSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request, pk):
    user = User.objects.get(pk=pk)

    serializer = UserDetailSerializer(user, many=False)

    return JsonResponse(serializer.data, safe=False)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editUser(request, pk):
    try: 
        name = request.data.get('name')
        avatar = request.FILES.get('avatar')
        user = User.objects.get(pk=pk)
        if name:
            user.name = name
        if avatar.size > 0:
            user.avatar = avatar
        user.save()
        serializer = UserDetailSerializer(user, many=False)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        print(str(e))
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['POST'])
@permission_classes([])
def createUser(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        user = User(email=email, password=password)
        user.save()
        serializer = UserDetailSerializer(user, many=False)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        print(str(e))
        return JsonResponse({"error": str(e)}, status=500)


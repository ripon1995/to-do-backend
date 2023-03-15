from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from hobby.models import Hobby
from hobby.serializers import HobbySerializer
from django.http import JsonResponse


@csrf_exempt
def hobby_views(request):
    if request.method == 'GET':
        hobby_data = Hobby.objects.all()
        serializer = HobbySerializer(hobby_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        print("Inside post")
        data = JSONParser().parse(request)
        serializer = HobbySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

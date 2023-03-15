from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from todo.models import ToDo
from todo.serializers import ToDoSerializer
from django.http import JsonResponse


# Create your views here.
@csrf_exempt
def to_do_list(request):
    if request.method == 'GET':
        to_do_list_data = ToDo.objects.all()
        serializer = ToDoSerializer(to_do_list_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        print("Inside post")
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

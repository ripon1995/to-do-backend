from todo.models import ToDo
from todo.serializers import ToDoSerializer
from django.http import JsonResponse


# Create your views here.

def to_do_list(request):
    if request.method == 'GET':
        to_do_list_data = ToDo.objects.all()
        serializer = ToDoSerializer(to_do_list_data, many=True)
        return JsonResponse(serializer.data, safe=False)

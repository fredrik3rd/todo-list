from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Todo.serializers import TaskSerializer
from Todo.models import Task

@csrf_exempt
def taskApi(request,id=0):
    if request.method=='GET':
        task = Task.objects.all()
        task_serializer=TaskSerializer(task,many=True)
        return JsonResponse(task_serializer.data,safe=False)
    elif request.method=='POST':
        task_data=JSONParser().parse(request)
        task_serializer=TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        task_data=JSONParser().parse(request)
        task=Task.objects.get(id=id)
        task_serializer=TaskSerializer(task,data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        task=Task.objects.get(id=id)
        task.delete()
        return JsonResponse("Deleted Successfully",safe=False)
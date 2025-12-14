from Task.models import Task
from django.shortcuts import get_object_or_404
from Task.serializers import TaskSerializer
from rest_framework.response import Response


def tasks_list(user):
    tasks = Task.objects.filter(user=user).select_related(
        'user'
    )
    serializer = TaskSerializer(tasks , many=True)
    return Response(serializer.data , status=200)

def create_task(data,user) : 
    serializer = TaskSerializer(data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=user)
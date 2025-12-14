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

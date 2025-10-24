from Task.models import Task
from django.shortcuts import get_object_or_404
from Task.serializers import TaskSerializer
from rest_framework.response import Response

def task_list(request) :
    
    tasks = Task.objects.select_related("user").all()
    serializer = TaskSerializer(tasks , many = True)
    return Response(serializer.data , status=200)


def create_task(request,data):
    user  = request.user
    serializer = TaskSerializer(user=user)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

def update_task(task_id, data):
    task = Task.objects.get(id=task_id)
    for key, value in data.items():
        setattr(task, key, value)
    task.save()
    return task

def delete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return True

def get_task(task_id):
    return get_object_or_404(Task, id=task_id)

def toggle_task_completion(task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True if not task.completed else False
    task.save()
    return task

def completed_tasks_list(request) :
    tasks = Task.objects.select_related("user").value("title","completed")
    serializer = TaskSerializer(tasks) 
    return Response(serializer.data , status=200)
    
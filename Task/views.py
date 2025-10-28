
from django.conf import settings
# rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# local imports 
from .serializers import TaskSerializer
from .models import Task
from .services.services import task_list, create_task, update_task, delete_task , get_task, completed_tasks_list


class task_list_create(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(user=request.user)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        tasks = Task.objects.select_related("user").all()
        serializer = TaskSerializer(tasks , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from 
from .serializers import TaskSerializer
from .models import Task
from .services.services import task_list, create_task, update_task, delete_task

class TaskListCreateView(APIView):
    def get(self, request):
        tasks = task_list()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        task = create_task(request, request.data)
        return Response(status=status.HTTP_201_CREATED)

class TaskDetailView(APIView):
    def put(self, request, pk):
        serializer = TaskSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            task = update_task(pk, serializer.validated_data)
            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_task(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)



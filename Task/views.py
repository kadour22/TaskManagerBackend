
from django.conf import settings
from django.shortcuts import get_object_or_404
# rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# local imports 
from .serializers import TaskSerializer, ChallengeSerializer
from .models import Task , Challenge

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


class mark_task_as_completed(APIView):
    permission_classes= [IsAuthenticated]
    def post(self,request,task_id) :
        task = get_object_or_404(Task,id=task_id)
        task.completed = True
        task.save()
        return Response("task updated")

class chanllenges_list_view(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request) :
        queryset = Challenge.objects.select_related(
            'user'
        ).all()
        serializer = ChallengeSerializer(queryset , many=True)
        return Response (serializer.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ChallengeSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(user=request.data)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
             
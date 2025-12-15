
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
from .services.services import tasks_list , create_task , mark_task_as_completed

class task_list_create(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request):
        return create_task(data=request.data,user=request.user)

    def get(self,request):
        return tasks_list(user=request.user)


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
             
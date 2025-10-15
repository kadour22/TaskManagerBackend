from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'user',"scheduled_time"]
        read_only_fields = ['id', 'created_at', 'updated_at','user',"scheduled_time"]
    
    def validate(self,data) :
        if data["title"] == "":
            raise serializers.ValidationError("Title cannot be empty")
        if data["description"] == "":
            raise serializers.ValidationError("Description cannot be empty")
        return data
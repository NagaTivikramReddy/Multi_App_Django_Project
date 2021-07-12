from rest_framework import serializers
# from .views import TaskList
from todolist.models import Task


class TaskSerializer(serializers.ModelSerializer):

    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created', 'completed']


class TaskCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id']
        ready_only_fields = ['title', 'description', 'created', 'completed']

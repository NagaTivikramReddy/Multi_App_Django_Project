from django.forms.models import model_to_dict
from todolist.models import Task
from .serializers import TaskCompleteSerializer, TaskSerializer
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError


class TaskListCreate(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

    def perform_craete(self, serializer):
        serializer.save(user=self.request.user)


class TaskListCompleted(generics.ListAPIView):
    model = Task
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user, completed__exact=True)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    model = Task
    serializer_class = TaskSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        item = Task.objects.filter(user=user)
        return item


class TaskComplete(generics.UpdateAPIView):
    model = Task
    serializer_class = TaskCompleteSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_update(self, task):

        if task.instance.completed == True:
            raise ValidationError("This taks is already completed")

        else:
            task.instance.completed = True
            task.save()

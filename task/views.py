from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

#Create your views here.
class TaskListView(generics.ListCreateAPIView):
   queryset = Task.objects.all()
   serializer_class = TaskSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

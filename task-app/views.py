from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

#Create your views here.

class TaskListView(generics.ListCreateAPIView): #Просмотр записей
   queryset = Task.objects.all()
   serializer_class = TaskSerializer

class TaskCreateView(generics.CreateAPIView):  #Создание записи
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):  #Изменение записи по ID
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):   #Удаление записи по ID
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


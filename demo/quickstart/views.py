from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Task, User
from .serializers import TaskSerializer, UserSerializer, UserTaskSerializer, TaskUserSerializer


# CRUD - Task
class TasksList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({'Tasks': serializer.data})

    def post(self, request, format=None): # create a task for an existing user
        user = request.data['user']
        user_instance = User.objects.get(email_address = user)
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task = task_serializer.save(user=user_instance)
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    def get(self, request, pk):
        tasks = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(tasks)
        return Response({'Task': serializer.data})


    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskUser(APIView):
    def get(self, request):
        user = User.objects.get(email_address='rida@gmail.com')
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({'Tasks of a user': serializer.data})


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserTaskSerializer(data=request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskUserSerializer

    @action(detail=False, methods=['GET'])
    def filter_tasks(self, request, **kwargs):
        queryset = self.get_queryset().filter(title='django')
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email_address'
    lookup_value_regex = '[\w.@]+'


class UserTaskViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserTaskSerializer


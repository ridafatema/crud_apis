from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'task', 'created_at')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)


class TaskUserSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'task', 'created_at', 'user')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email_address')

    def validate_email_address(self, value):
        if 'gmail' not in value:
            raise serializers.ValidationError('This Email Address is not a Gmail id')
        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class UserTaskSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = User
        fields = ('name', 'email_address', 'tasks')

    def create(self, validated_data):
        task_data = validated_data.pop('tasks')
        user = User.objects.create(**validated_data)
        for task in task_data:
            Task.objects.create(user=user, **task)
        return user

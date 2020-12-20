from django.urls import path, include
from rest_framework import routers
from .views import TasksList, TaskDetail, TaskUser, UserList, TaskViewSet, UserViewSet, UserTaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'task-user', UserTaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('tasklist', TasksList.as_view()),
    path('task/<int:pk>', TaskDetail.as_view()),
    path('taskuser', TaskUser.as_view()),
    path('user', UserList.as_view()),
]

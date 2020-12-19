from django.urls import path, include
from .views import TasksList, TaskDetail, TaskUser, UserList

urlpatterns = [
    path('tasklist', TasksList.as_view()),
    path('task/<int:pk>', TaskDetail.as_view()),
    path('tasku', TaskUser.as_view()),
    path('user', UserList.as_view()),
]

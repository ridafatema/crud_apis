from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from .views import TasksList, TaskDetail, TaskUser, UserList, TaskViewSet, UserViewSet, UserTaskViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'users', UserViewSet, basename='users')
router.register(r'task-user', UserTaskViewSet, basename='task')

schema_view = get_schema_view(title='Tasks API',
                description='An API to write tasks.')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
    path('tasklist', TasksList.as_view()),
    path('task/<int:pk>', TaskDetail.as_view()),
    path('taskuser', TaskUser.as_view()),
    path('user', UserList.as_view()),
    path('docs/', include_docs_urls(title='Tasks API'))
]

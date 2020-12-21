from django.contrib import admin

# Register your models here.
from quickstart.models import User, Task

admin.site.register(User)
admin.site.register(Task)

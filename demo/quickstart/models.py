from django.db import models


class User(models.Model):
    name = models.CharField(max_length = 20)  # cannot be left blank as default is FALSE
    email_address = models.EmailField(primary_key=True)       # NULL is also by default FALSE
    password = models.CharField(max_length=20)

    def __str__(self):
        return "{} & {} ". format(self.name, self.email_address)


class Task(models.Model):
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE) # fk is email-address
    title = models.CharField(max_length=20)
    task = models.TextField(max_length=30)
    created_at = models.DateField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "{} - {} - {} - {} - {}". format(self.title, self.task, self.created_at, self.user, self.id)


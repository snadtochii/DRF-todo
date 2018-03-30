from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    users = models.ManyToManyField(
        User,
        related_name='tasks',
        blank=True
    )
    creator = models.ForeignKey(
        User,
        related_name='my_tasks',
        on_delete=models.CASCADE
    )

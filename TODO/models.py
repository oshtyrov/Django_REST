from django.db import models
from usersapp.models import CustomUser
from uuid import uuid4


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=32, unique=True)
    users = models.ManyToManyField(CustomUser)
    repository = models.URLField(blank=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    ia_active = models.BooleanField(default=True)

from django.db import models
from django.db import models as m
from django.contrib.auth.models import User


class Group(m.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(m.Model):
    user = models.CharField(max_length=255)

    def __str__(self):
        return self.user


class Student(m.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pasport_id = models.IntegerField()
    balance = models.IntegerField()
    deboting = models.BooleanField()

    def __str__(self) -> str:
        return self.full_name

from django.db import models as m
from student.models import Group


class Course(m.Model):
    name = m.CharField(max_length=255)
    groups = m.ManyToManyField(Group)

    def __str__(self):
        return f"{self.name} : {self.groups.count()}"

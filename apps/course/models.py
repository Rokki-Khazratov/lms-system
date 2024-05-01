from django.db import models as m
from apps.student.models import Group, Teacher


TEST_CHOISES=[
    (1,'Written'),
    (2,'Oral'),
    (3,'Selfwork'),
]

EXAM_CHOISES=[
    (1,'Midtearm'),
    (2,'Final'),
]

class Course(m.Model):
    name = m.CharField(max_length=255)
    groups = m.ManyToManyField(Group)

    def __str__(self):
        return f"{self.name} : {self.groups.count()}"
    
class Room(m.Model):
    name = m.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Subject(m.Model):
    name = m.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Schedule(m.Model):
    teacher = m.ForeignKey(Teacher, on_delete=m.CASCADE)
    subject = m.ForeignKey(Subject, on_delete=m.CASCADE)
    room = m.ForeignKey(Room, on_delete=m.CASCADE)
    date = m.DateField()
    time_start = m.TimeField()
    time_end = m.TimeField()

    def __str__(self):
        return f"{self.subject} - {self.teacher} - {self.date} {self.time_start}-{self.time_end}"
    
class Exam(m.Model):
    subject = m.ForeignKey(Subject, on_delete=m.CASCADE)
    room = m.ForeignKey(Room, on_delete=m.CASCADE)
    date = m.DateField()
    time_start = m.TimeField()
    time_end = m.TimeField()
    test_choises = m.IntegerField(choices=TEST_CHOISES)
    exam_choises = m.IntegerField(choices=EXAM_CHOISES)

    def __str__(self):
        return f"Экзамен по {self.subject} - {self.date} {self.time_start}-{self.time_end}"



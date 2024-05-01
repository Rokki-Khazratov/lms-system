from django.db import models
from django.db import models as m
from django.contrib.auth.models import User

LANGUAGE_CHOISES=[
    (1,'Uzbek'),
    (2,'Russian'),
    (3,'English'),
]

GROUP_CHOISES=[
    (1,'Zaochniy'),
    (2,'Ochniy'),
]

TEST_CHOISES=[
    (1,'Written'),
    (2,'Oral'),
    (3,'Selfwork'),
]

EXAM_CHOISES=[
    (1,'Midtearm'),
    (2,'Final'),
]

class Group(m.Model):
    name = models.CharField(max_length=255)
    language = models.IntegerField(choices=LANGUAGE_CHOISES)
    group_type = models.IntegerField(choices=GROUP_CHOISES)
    tutor = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='teacher_images/')
    is_tutor = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_tutor_groups(self):
        if self.is_tutor:
            # Получаем количество групп, в которых может быть учитель
            max_groups = 15
            # Фильтруем группы по текущему учителю и ограничиваем количество
            return Group.objects.filter(tutor=self)[:max_groups]
        else:
            return None


class User(m.Model):
    user = models.CharField(max_length=255)

    def __str__(self):
        return self.user


class Student(m.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pasport_id = models.CharField()
    balance = models.IntegerField()
    deboting = models.BooleanField()

    def __str__(self) -> str:
        return self.full_name
    
class Room(m.Model):
    name = m.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Subject(m.Model):
    name = m.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return f"{self.subject} - {self.teacher} - {self.date} {self.time_start}-{self.time_end}"
    
class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    test_choises = models.IntegerField(choices=TEST_CHOISES)
    exam_choises = models.IntegerField(choices=EXAM_CHOISES)

    def __str__(self):
        return f"Экзамен по {self.subject} - {self.date} {self.time_start}-{self.time_end}"


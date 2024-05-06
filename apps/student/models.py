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

class Group(m.Model):
    name = models.CharField(max_length=255)#
    language = models.IntegerField(choices=LANGUAGE_CHOISES) #
    group_type = models.IntegerField(choices=GROUP_CHOISES) #
    tutor = models.ForeignKey('Teacher', on_delete=models.CASCADE) #

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)#
    img = models.ImageField(upload_to='teacher_images/')
    is_tutor = models.BooleanField(default=False)#

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




class Student(m.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True) #
    full_name = models.CharField(max_length=55) #
    phone_number = models.CharField(max_length=55)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pasport_id = models.CharField(max_length=255) #
    balance = models.IntegerField()
    deboting = models.BooleanField() #

    def __str__(self):
        return self.full_name
    

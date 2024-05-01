from django.contrib import admin
from apps.course.models import *
from apps.student.models import *

admin.site.register(Course)
admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Exam)

admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Student)
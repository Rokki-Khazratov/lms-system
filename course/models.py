from django.db import models
from django.db import models as m



class Course(m.Model):
    name = models.CharField(max_length=255)
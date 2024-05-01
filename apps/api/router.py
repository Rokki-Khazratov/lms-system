from django.urls import path
from .views import *
from apps.course.views import *
from apps.student.views import *

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>', StudentRUDView.as_view(), name='student-rud'),
]
from django.urls import path
from .views import *
from apps.course.views import *
from apps.student.views import *

urlpatterns = [
##################################STUDENT##################################

    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>', StudentRUDView.as_view(), name='student-rud'),

    path('teachar/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachar/<int:pk>', TeacherRUDView.as_view(), name='teacher-rud'),

    path('group/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('group/<int:pk>', GroupRUDView.as_view(), name='student-rud'),

##################################COURSE##################################

    path('exam/', ExamListCreateAPIView.as_view(), name='exam-list-create'),
    path('exam/<int:pk>', ExamRUDView.as_view(), name='exam-rud'),

    path('schedule/', ScheduleListCreateAPIView.as_view(), name='schedule-list-create'),
    path('schedule/<int:pk>', ScheduleRUDView.as_view(), name='schedule-rud'),

    path('subject/', SubjectListCreateAPIView.as_view(), name='subject-list-create'),
    path('subject/<int:pk>', SubjectRUDView.as_view(), name='subject-rud'),

    path('course/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('course/<int:pk>', CourseRUDView.as_view(), name='course-rud'),

    path('room/', RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('room/<int:pk>', RoomRUDView.as_view(), name='room-rud'),

]
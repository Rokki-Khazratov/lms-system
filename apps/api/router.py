from django.urls import path
from .views import *
from apps.course.views import *
from apps.student.views import *

urlpatterns = [
##################################STUDENT##################################

    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>', StudentRUDView.as_view(), name='student-rud'),

    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>', TeacherRUDView.as_view(), name='teacher-rud'),

    path('groups/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('groups/<int:pk>', GroupRUDView.as_view(), name='student-rud'),

##################################COURSE##################################

    path('exams/', ExamListCreateAPIView.as_view(), name='exam-list-create'),
    path('exams/<int:pk>', ExamRUDView.as_view(), name='exam-rud'),

    path('schedules/', ScheduleListCreateAPIView.as_view(), name='schedule-list-create'),
    path('schedules/<int:pk>', ScheduleRUDView.as_view(), name='schedule-rud'),

    path('subjects/', SubjectListCreateAPIView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>', SubjectRUDView.as_view(), name='subject-rud'),

    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>', CourseRUDView.as_view(), name='course-rud'),

    path('rooms/', RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>', RoomRUDView.as_view(), name='room-rud'),

]
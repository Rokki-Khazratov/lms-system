from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .serializer import ScheduleSerializer, SubjectSerializer, ExamSerializer, RoomSerializer, CourseSerializer
from .models import Exam, Schedule, Subject, Course, Room

class ScheduleListCreateAPIView(ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.all()

        teacher = self.request.query_params.get('teacher', None)
        room = self.request.query_params.get('room', None)
        date = self.request.query_params.get('date', None)
        time_start = self.request.query_params.get('time_start', None)
        time_end = self.request.query_params.get('time_endt', None)
        if teacher:
            queryset = queryset.filter(teacher=teacher)
        if room:
            queryset = queryset.filter(room=room)
        if date:
            queryset = queryset.filter(date=date)
        if time_start:
            queryset = queryset.filter(time_start=time_start)
        if time_end:
            queryset = queryset.filter(time_endt=time_end)

        return queryset


class ScheduleRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ExamListCreateAPIView(ListCreateAPIView):
    serializer_class = ExamSerializer
    
    
    def get_queryset(self):
        queryset = Exam.objects.all()

        subject = self.request.query_params.get('subject', None)
        room = self.request.query_params.get('room', None)
        test_choises = self.request.query_params.get('test_choises', None)
        exam_choises = self.request.query_params.get('exam_choises', None)
        
        if subject:
            queryset = queryset.filter(subject=subject)
        if room:
            queryset = queryset.filter(room=room)
        if test_choises:
            queryset = queryset.filter(test_choises=test_choises)
        if exam_choises:
            queryset = queryset.filter(exam_choises=exam_choises)

        return queryset

class ExamRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class SubjectListCreateAPIView(ListCreateAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        name = self.request.query_params.get('name', None)

        if name:
            queryset = queryset.filter(name=name)

        return queryset

class SubjectRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseListCreateAPIView(ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        name = self.request.query_params.get('name', None)
        groups = self.request.query_params.get('groups', None)

        if name:
            queryset = queryset.filter(name=name)
        if groups:
            queryset = queryset.filter(groups=groups)

        return queryset

class CourseRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RoomListCreateAPIView(ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        name = self.request.query_params.get('name', None)

        if name:
            queryset = queryset.filter(name=name)

        return queryset


class RoomRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
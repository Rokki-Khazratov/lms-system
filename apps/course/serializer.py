from rest_framework import serializers
from .models import Exam, Schedule, Subject, Course, Room



class ExamSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    class Meta:
        model = Exam
        fields = ['id', 'subject', 'room', 'date', 'time_start', 'time_end', 'test_choises', 'exam_choises']

    def get_subject(self,obj):
        return obj.subject.name


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'teacher', 'subject', 'room', 'date', 'time_start', 'time_end']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'groups']


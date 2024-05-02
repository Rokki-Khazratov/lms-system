from rest_framework import serializers
from .models import Exam, Schedule, Subject, Course, Room


class ExamSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
    test_choises = serializers.SerializerMethodField()
    exam_choises = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = ['id', 'subject', 'room', 'date', 'time_start', 'time_end',
                  'test_choises', 'exam_choises']

    def get_subject(self, obj):
        return obj.subject.name

    def get_room(self, obj):
        return obj.room.name

    def get_test_choises(self, obj):
        return dict(Exam._meta.get_field('test_choises').choices).get(obj.test_choises)

    def get_exam_choises(self, obj):
        return dict(Exam._meta.get_field('exam_choises').choices).get(obj.exam_choises)



class ScheduleSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['id', 'teacher',  'subject', 'room', 'date', 'time_start', 'time_end']

    def get_teacher(self, obj):
        return obj.teacher.name if obj.teacher else None

    def get_subject(self, obj):
        return obj.subject.name if obj.subject else None

    def get_room(self, obj):
        return obj.room.name if obj.room else None




class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'groups']

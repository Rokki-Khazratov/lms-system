from rest_framework import serializers
from .models import Student, Teacher, Group

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'group', 'full_name', 'phone_number', 'pasport_id', 'balance', 'deboting']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'img', 'is_tutor']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name','language', 'group_type', 'tutor']

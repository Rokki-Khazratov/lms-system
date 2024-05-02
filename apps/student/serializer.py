from rest_framework import serializers
from .models import Student, Teacher, Group

LANGUAGE_CHOICES = [
    (1, 'Uzbek'),
    (2, 'Russian'),
    (3, 'English'),
]

GROUP_CHOICES = [
    (1, 'Zaochniy'),
    (2, 'Ochniy'),
]

class StudentSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'group', 'full_name', 'phone_number', 'pasport_id', 'balance', 'deboting']

    def get_group(self,obj):
        return obj.group.name


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'img', 'is_tutor']


class GroupSerializer(serializers.ModelSerializer):
    language = serializers.SerializerMethodField()
    group_type = serializers.SerializerMethodField()
    tutor = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'language', 'group_type', 'tutor']

    def get_language(self, obj):
        return dict(LANGUAGE_CHOICES).get(obj.language)

    def get_group_type(self, obj):
        return dict(GROUP_CHOICES).get(obj.group_type)
    
    def get_tutor(self,obj):
        return obj.tutor.name

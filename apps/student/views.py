from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .serializer import StudentSerializer, TeacherSerializer, GroupSerializer
from .models import Student, Teacher, Group

class StudentListCreateAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    

    def get_queryset(self):
        queryset = Student.objects.all()

        group_id = self.request.query_params.get('group_id', None)
        full_name = self.request.query_params.get('full_name', None)
        pasport_id = self.request.query_params.get('pasport_id', None)
        deboting = self.request.query_params.get('deboting', None)

        if group_id:
            queryset = queryset.filter(group=group_id)

        if full_name:
            queryset = queryset.filter(full_name=full_name)

        if pasport_id:
            queryset = queryset.filter(pasport_id=pasport_id)

        if deboting is not None:
            deboting = deboting.lower() == 'true'  
            queryset = queryset.filter(deboting=deboting)

        return queryset



class StudentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherListCreateAPIView(ListCreateAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()

        name = self.request.query_params.get('name', None)
        is_tutor = self.request.query_params.get('is_tutor', None)

        if name:
            queryset = queryset.filter(name=name)

        if is_tutor is not None:
            is_tutor = is_tutor.lower() == 'true'  
            queryset = queryset.filter(is_tutor=is_tutor)

        return queryset
    

class TeacherRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        queryset = Group.objects.all()

        name = self.request.query_params.get('name', None)
        language = self.request.query_params.get('language', None)
        group_type = self.request.query_params.get('group_type', None)
        tutor_id = self.request.query_params.get('tutor_id', None)

        if name:
            queryset = queryset.filter(name=name)

        if language:
            queryset = queryset.filter(language=language)

        if group_type:
            queryset = queryset.filter(group_type=group_type)

        if tutor_id:
            queryset = queryset.filter(tutor_id=tutor_id)

        return queryset


class GroupRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
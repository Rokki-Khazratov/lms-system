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

        if deboting:
            queryset = queryset.filter(deboting=deboting)

        return queryset



class StudentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherListCreateAPIView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
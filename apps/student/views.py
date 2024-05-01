from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .serializer import StudentSerializer
from .models import Student

class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
from rest_framework import viewsets
from .models import Teacher, Student
from .serializers import TeacherSerializers, StudentSerializers
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as django_filters
from .filters import TeacherFilter, StudentFilter
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly


class CustomPagination(PageNumberPagination):
    page_size = 8


class TeacherViewSet(viewsets.ModelViewSet):
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filter_class = TeacherFilter
    search_fields = ['faculty', 'group', 'first_name', 'last_name']
    pagination_class = CustomPagination
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [IsStaffOrReadOnly]


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filter_class = StudentFilter
    search_fields = ['faculty', 'group', 'first_name', 'last_name']
    pagination_class = CustomPagination
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_class = [IsOwnerOrReadOnly]

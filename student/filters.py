from django_filters import rest_framework as django_filters
from .models import Student, Teacher


class StudentFilter(django_filters.Filter):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'science']


class TeacherFilter(django_filters.Filter):
    class Meta:
        model = Teacher
        fields = ['science', 'first_name', 'last_name']

from .models import Teacher, Student
from rest_framework.serializers import ModelSerializer


class TeacherSerializers(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

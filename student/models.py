from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    science = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    faculty = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.first_name

from django.urls import path, include
from rest_framework import routers
from .views import TeacherViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
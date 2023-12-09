from rest_framework import viewsets
from course.models import Courses
from course.serilzers import CoursesSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

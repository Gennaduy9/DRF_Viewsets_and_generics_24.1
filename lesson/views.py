from rest_framework import generics

from lesson.models import Lessons
from lesson.serilzers import LessonsSerializer


class LessonsListView(generics.ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsCreateView(generics.CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsUpdateView(generics.UpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsRetrieveView(generics.RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsDestroyView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer

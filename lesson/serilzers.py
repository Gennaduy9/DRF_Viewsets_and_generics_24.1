from rest_framework import serializers

from lesson.models import Lessons


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = (
            'name',
            'description'
        )
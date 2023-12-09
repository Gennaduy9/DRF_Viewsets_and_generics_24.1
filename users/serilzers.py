from rest_framework import serializers

from lesson.models import Lessons


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = (
            'email',
            'phone',
            'country'
        )
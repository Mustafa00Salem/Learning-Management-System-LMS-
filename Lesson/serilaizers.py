from rest_framework import serializers
from .models import Lesson

class LessonSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['course','title','description','video','order','is_preview','created_at','updated_at']
        
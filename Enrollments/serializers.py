from rest_framework import serializers
from .models import Enrollment
from Courses.serializer import CourseSerializer
from Courses.models import Course

class EnrollmentSerializer(serializers.ModelSerializer):
    course_info = CourseSerializer( read_only=True)
    course = serializers.IntegerField(write_only=True)
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'course_info', 'enrolled_at', 'is_active']
        read_only_fields = ['student', 'enrolled_at', 'is_active']
    
    def validate_course(self, course_id):
        try:
            course = Course.objects.get(id=course_id)
            return course
        except Course.DoesNotExist:
            raise serializers.ValidationError('Course ID Dose Note Exit')
    
    def validate(self, data):
        student = self.context['request'].user
        course = data.get('course')
        
        if Enrollment.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError({"course":"You Are Already Enrollment"})
        return data
    def create(self, validated_data):
        validated_data['student']= self.context['request'].user
        return super().create(validated_data)
        
        
        

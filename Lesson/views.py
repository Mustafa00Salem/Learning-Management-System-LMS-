from django.shortcuts import render
from rest_framework import generics
from .models import Lesson
from .serilaizers import LessonSerilaizer
from rest_framework.permissions import IsAuthenticated
from Courses.permission import IsTeacher, IsCourseOwner
# Create your views here.


class GetLesson(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerilaizer
    permission_classes = [IsAuthenticated]
    
    
class CreateLesson(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerilaizer
    permission_classes = [IsTeacher,IsCourseOwner]
    
    
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment
from .serializers import EnrollmentSerializer
from Courses.permission import IsStudent

# Create your views here.

class EnrollmentCourse(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes= [IsAuthenticated]
    
    

class EnrollmentCourseList(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes= [IsAuthenticated, IsStudent]
    
    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)
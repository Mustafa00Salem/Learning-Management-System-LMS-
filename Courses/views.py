from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Course, Review
from .serializer import CourseSerializer, ReviewCreateSerializer, ReviewSerializer
from .pagination import StandardPagination
from .filters import CourseFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permission import IsTeacher, IsStudent, IsCourseOwner
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.


class ListCreateCourses(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StandardPagination
    
    filterset_class = CourseFilter
    filter_backends= [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']     
    ordering_fields = ['price', 'name', 'created_at']
    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)
        
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsTeacher()]
        return [AllowAny()]
    
    
class GetPutDeleteCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_permissions(self):
        if self.request.method in  ["PUT", "PATCH", "DELETE"]:
            return[
                IsAuthenticated(), IsTeacher(),IsCourseOwner()
            ]
        return [AllowAny()]
    
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]   

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.prefetch_related('reviews')  
    serializer_class = CourseSerializer
    lookup_field = 'slug'
    
    
    
    
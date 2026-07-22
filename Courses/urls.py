from django.urls import path
from . import views


urlpatterns = [
    path('list_create_course/',views.ListCreateCourses.as_view(), name='list_create_course'),
    path('put_delete_course/<str:pk>/', views.GetPutDeleteCourse.as_view(), name='put_delete_course'),
    path('review/<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('add_review/<int:course_id>/', views.ReviewCreateView.as_view(), name='add-review'),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('enrolment/', views.EnrollmentCourse.as_view(), name='enrolment'),
    path('list_enrolment/', views.EnrollmentCourseList.as_view(), name='enrolment'),
]

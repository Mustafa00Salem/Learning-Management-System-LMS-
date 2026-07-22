from django.urls import path
from . import views

urlpatterns = [
    path('git_lesson', views.GetLesson.as_view(), name='git_lesson'),
    path('create_lesson', views.CreateLesson.as_view(), name='create_lesson')
]

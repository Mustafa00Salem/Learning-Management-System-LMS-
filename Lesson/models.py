from django.db import models
from Courses.models import Course
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Lesson(models.Model):
    course = models.ForeignKey(Course,  on_delete=models.CASCADE, related_name="lessons") 
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.URLField()
    order = models.PositiveIntegerField(default=1)
    is_preview = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
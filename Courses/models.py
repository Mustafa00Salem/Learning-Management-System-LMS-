from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


User = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30,unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args,**kwargs)
        
    
class Course(models.Model):
    name = models.CharField(max_length=99, null=False, blank=False)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='courses' )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='course_img', blank= True, null= True)
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1 
            while Course.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)        
    def average_rating(self):
        return self.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0

class Review(models.Model):
    RATING_CHOICES = [
        (1, "1 - Poor"),
        (2, "2 - Fair"),
        (3, "3 - Good"),
        (4, "4- Very Good"),
        (5, "5 - Excellent")
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='reviews')
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        unique_together = ("user", "course")
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.rating} - Review - {self.course.name}'
    def average_rating(self):
        return self.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0

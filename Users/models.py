from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save



class User(AbstractUser):

    ROLE_CHOICES = (
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
    )
    profile_picture= models.ImageField(    upload_to="profile_pictures/",blank=True,null=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES, blank=False, null=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    reset_password_sent = models.CharField(max_length=45, default='',blank=True)
    expire_rest_password = models.DateTimeField(null=True, blank=True)
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

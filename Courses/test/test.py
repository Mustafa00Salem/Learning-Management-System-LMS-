from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

User = get_user_model()

class BaseTest(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(
            first_name='student', 
            last_name= 'user',
            username='student@gmail.com',
            password = "Passw12345",
            role = 'STUDENT'
        )
        self.teacher = User.objects.create_user(
            first_name='teacher', 
            last_name= 'user',
            username='teacher@gmail.com',
            password = "Passw12345",
            role = 'TEACHER'
        )
        refresh = RefreshToken.for_user(self.student)
        self.student_access_token = str(refresh.access_token)
        self.refresh_token = str(refresh)
        
        refresh_teacher = RefreshToken.for_user(self.teacher)
        self.access_token_teacher = str(refresh_teacher.access_token)
        self.refresh_token_teacher = str(refresh_teacher)
        
    def get_auth_client(self, token=None):
        client = APIClient()
        if token:
            client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        return client
    
class CouresTest(BaseTest):
    def test_get_course(self):
        client = self.get_auth_client(self.student_access_token)
        course = reverse('list_create_course')
        response = client.get(course)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_add_course(self):
        client = self.get_auth_client(self.access_token_teacher)
        course = reverse('list_create_course')
        data = {
            "name": "Nano",
            "description": "learning new Nano Dentistery in 2026",
            "price": "600.55",
            'instructor':"user",
            "slug":"nano_pass"
 
        }
        response = client.post(course, data)
        response = self.client.post(course, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
        
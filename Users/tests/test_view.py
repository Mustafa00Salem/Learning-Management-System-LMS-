from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name = 'user',
            last_name = 'name',
            email = 'user@gmail.com',
            password = "Passw12345",
            role = 'STUDENT'
        )        
        self.user.set_password("Passw12345")
        self.user.save()
        
        self.admin_user = User.objects.create_superuser(
            first_name = "admin",
            last_name = "name",
            email= "admin@gmail.com",
            username='admin@gmail.com',
            password="Passw12345"
        )
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.refresh_token = str(refresh)
        
        refresh_admin = RefreshToken.for_user(self.admin_user)
        self.admin_access_token = str(refresh_admin.access_token)
        
    def get_auth_client(self, token=None):
        client = APIClient()
        if token:
            client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        return client
    
class RegisterTests(BaseTest):
    def test_register_success(self):
        url = reverse('register')
        data = {
            "first_name":"user",
            "last_name":"name",
            "email":"user@gmail.com",
            "password":"User12345",
            "role":"STUDENT"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data'], "Your Register Successfuly")
        
    def test_register_invalid_data(self):
        url = reverse('register')
        data={'email':"user@gmail.com",'password':"User12345"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class ProfileTest(BaseTest):
    def test_profile_success(self):
        url= reverse('profile')
        client = self.get_auth_client(self.access_token)
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'user@gmail.com')
        self.assertEqual(response.data['role'], 'STUDENT')
    def test_profile_unauthorize(self):
        url= reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
class UserDetailTest(BaseTest):
    def test_user_detail_admin(self):
        url = reverse('userdetail', kwargs={'pk':self.user.id})
        client = self.get_auth_client(self.admin_access_token)
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail_as_normal_user(self):
        url = reverse('userdetail', kwargs={'pk': self.admin_user.id})
        client = self.get_auth_client(self.access_token) 
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ChangePasswordTest(BaseTest):
    def test_change_password_success(self):
        url = reverse('changepassword')
        client = self.get_auth_client(self.access_token)
        data={
            "old_password":"Passw12345",
            "new_password":"KPassw12345",
            "confirm_password":"KPassw12345"
            }
        response = client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LogoutTest(BaseTest):

    def test_logout_success(self):
        url = reverse("logout")
        client = self.get_auth_client(self.access_token)

        response = client.post(url, {
            "refresh": self.refresh_token
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

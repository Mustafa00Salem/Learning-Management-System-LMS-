from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChangePasswordSerializers, RegisterSerializer, ProfileSerializers, LogoutSerilaizer
from rest_framework import status

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

# Create your views here.

User = get_user_model()

class Register(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({'data':"Your Register Successfuly"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
    
  
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(username=email, password=password)
        if user is None:
            return Response({'Error':'Invalid Username Or Password'}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
        
class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = ProfileSerializers(request.user)
        return Response(serializer.data)
        
class UserDetail(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = ProfileSerializers(user)
        return Response(serializer.data)
    
class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        serializer = ChangePasswordSerializers(data = request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data["old_password"]):
                return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            
            return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAccount(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request):

        request.user.delete()
        return Response(
            {
                "message": "Account deleted successfully."
            },
            status=status.HTTP_200_OK
        )
        
class Logout(APIView):
    permission_classes= [IsAuthenticated]
    def post(self, request):
        serializer = LogoutSerilaizer(data=request.data)
        if serializer.is_valid():
            token = RefreshToken(serializer.validated_data['refresh'])
            token.blacklist()
            return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

def get_correct_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return f"{protocol}://{host}"

class ForgitPassword(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        data = request.data
        user = get_object_or_404(User, email=data['email'])
        token = get_random_string(40)
        expire_date = datetime.now() + timedelta(minutes=30)
        user.profile.reset_password_sent = token
        user.profile.expire_rest_password = expire_date
        user.profile.save()
        link = f"{get_correct_host(request)}/resetpassword/{token}"
        send_mail(
            subject="Reset Password",
            message=f"Your reset password link is: {link}",
            from_email="LMS@gmail.com",
            recipient_list=[data["email"]],
        )
        return Response(
            {"detail": "Password reset email sent.","email": data["email"]},status=status.HTTP_200_OK )
        
class ResetPassword(APIView):
    permission_classes=[AllowAny]
    def post(self, request, token):
        data = request.data
        user = get_object_or_404(User, profile__reset_password_sent = token)
        
        if user.profile.expire_rest_password.replace(tzinfo=None)  < datetime.now():
           return Response( {"Error": "time is expire"},status=status.HTTP_400_BAD_REQUEST)
        if data['password'] != data['confirmpassword']:
           return Response( {"Error": "password not equal confirm password"},status=status.HTTP_400_BAD_REQUEST)
            
        user.password = make_password(data['password'])
        user.profile.reset_password_sent = ''
        user.profile.expire_rest_password = None
        user.profile.save()
        user.save()
        return Response( {"data": "password reset done"})
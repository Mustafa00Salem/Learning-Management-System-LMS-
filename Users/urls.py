from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path("logout/", views.Logout.as_view(), name="logout"),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('userdetail/<str:pk>', views.UserDetail.as_view(), name='userdetail'),
    path('changepassword/', views.ChangePassword.as_view(), name='changepassword'),
    path('deletepassword/', views.DeleteAccount.as_view(), name='deletepassword'),
    path('forgetpassword/', views.ForgitPassword.as_view(), name='forgetpassword'),
    path('resetpassword/<str:token>', views.ResetPassword.as_view(), name='resetpassword'),
]

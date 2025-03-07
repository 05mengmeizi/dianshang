from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('check-login/', views.CheckLoginStatusView.as_view(), name='check-login'),
    path('info/', views.UserInfoView.as_view(), name='user-info'),
] 
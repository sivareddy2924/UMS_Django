from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('loginregistration/', views.loginregistration, name='loginregistration'),  # Login/Registration page
    path('loginregistration/register', views.register, name='register'),  # Registration
    path('login/', views.user_login, name='login'),  # Login
    path('logout/', views.logout_user, name='logout'),  # Logout
    path('student/dashboard', views.student_dashboard, name='student_dashboard'),  # Student dashboard
    path('courselist', views.course_list, name='course_list'),  # Student dashboard
   
]
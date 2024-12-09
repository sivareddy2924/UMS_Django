from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserDetail  
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def loginregistration(request):
    return render(request,'login-registration.html') 

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Create a new User
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()

        # Link to UserDetail model
        UserDetail.objects.create(
            auth_user=user,
            fname=fname,
            lname=lname,
            username=username,
            password=password,
            role=role
        )

        
    return render(request, 'login-registration.html')

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # return HttpResponse(user)
        if user is not None:
            login(request, user) 
            # Check the role from the user's profile
            try:
                # Fetch the user's ID and their associated role
                auth_id = User.objects.get(username=username).id
                auth_role = UserDetail.objects.get(auth_user_id=auth_id).role

                # Redirect based on the user's role
                if auth_role == 'student':  # If role is student
                    return redirect('student_dashboard')  # Redirect to student dashboard
                elif auth_role == 'teacher':  # If role is teacher
                    return redirect('/teacher+dashboard/')  # Redirect to teacher dashboard
                elif username == 'admin':  # If role is admin
                    return redirect('/admin_dashboard/')  # Redirect to admin dashboard
                else:
                    return redirect('index')  # If no role is found, redirect to the index page
            except UserDetail.DoesNotExist:
                return redirect('index')  # Redirect to index if user detail does not exist

        else:
            return redirect('index')  # If authentication fails, redirect to the login page

    return render(request, 'login-registration.html')

def student_dashboard(request):
    return render(request,'student/dashboard.html')

# Logout view
def logout_user(request):
    logout(request)
    return redirect('/')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courselist.html', {'courses': courses})
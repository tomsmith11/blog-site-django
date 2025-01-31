from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # Use Django's User model
from .models import Blog 
# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # Django's User
from .models import Blog

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')

        user = User.objects.create_user(
            username=email,  # Using email as username
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return redirect('login')
    return render(request, 'ecommerce/form/register.html')

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if request.user.is_authenticated:
            Blog.objects.create(title=title, content=content, author=request.user)
            return redirect('blogs')
    return render(request, 'ecommerce/form/blog_create.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate using username (email in this case)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            return HttpResponse('Invalid credentials')
            
    return render(request, 'ecommerce/form/login.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'ecommerce/blog_list.html', {'blogs': blogs})

def logout_view(request):
    logout(request)
    return redirect('login')


def index(request):
  return render(request, 'ecommerce/index.html')

def home(request):
  return render(request, 'ecommerce/home.html')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'ecommerce/blogs.html', {'blogs': Blog.objects.all()})

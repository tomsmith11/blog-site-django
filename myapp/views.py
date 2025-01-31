from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # Use Django's User model
from .models import Product
# Create your views here.

def register_view(request):  # Separate registration view
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')

        # Create user using Django's User model
        user = User.objects.create_user(
            username=email,  # Using email as username
            email=email,
            password=password,  # This will hash the password automatically
            first_name=first_name,
            last_name=last_name
        )

        
        return redirect('login')
    return render(request, 'ecommerce/form/register.html')

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

def logout_view(request):
    logout(request)
    return redirect('login')


def index(request):
  return render(request, 'ecommerce/index.html')

def home(request):
  return render(request, 'ecommerce/home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/products.html', {'products': Product.objects.all()})
def about(request):
  return render(request, 'ecommerce/about.html')

def contact(request):
  return render(request, 'ecommerce/contact.html')

def our_story(request):
  return render(request, 'ecommerce/our_story.html')

def careers(request):
  return render(request, 'ecommerce/careers.html')

def returns(request):
  return render(request, 'ecommerce/returns.html')

def press(request):
  return render(request, 'ecommerce/press.html')

def shipping(request):
  return render(request, 'ecommerce/shipping.html')
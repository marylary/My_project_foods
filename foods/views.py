from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from foods.models import Person

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def shop(request):
    return render(request, 'pages/shop/shop.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blogs/blog.html')

def blogsingle(request):
    return render(request, 'pages/blogs/blogs-single.html')

def contact(request):
    return render(request, 'pages/contact.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/shop/checkout.html')

def product(request):
    return render(request, 'pages/shop/single-product.html')

def wishlist(request):
    return render(request, 'pages/shop/wishlist.html')

def single(request):
    return render(request, 'pages/blogs/blogs-single.html')

# users
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # form = Person(data=request.POST)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, 'Votre compte a ete bien creer!!!')
        #     return redirect('login')
    return render(request, 'users/register.html',)

def connect(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenu')
            return redirect('home')
        else:
            messages.error(request, "Erreur d'authentification")
    return render(request, 'users/login.html')    
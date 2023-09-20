from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'fromagerie/index.html')

def contact(request):
    return render(request, 'fromagerie/contact.html')

def login(request):
    return render(request, 'fromagerie/login.html')
def signup(request):
    return render(request, 'fromagerie/signup.html')
def recoverpassword(request):
    return render(request, 'fromagerie/recoverpassword.html')
def about(request):
    return render(request, 'fromagerie/about.html')
def shop(request):
    return render(request, 'fromagerie/shop.html')

def carrito(request):
    return render(request, 'fromagerie/carrito.html')


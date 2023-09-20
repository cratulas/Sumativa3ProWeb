from django.shortcuts import render, redirect
from .forms import ContactFormModel

# Create your views here.

def index(request):
    return render(request, 'fromagerie/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactFormModel()

    return render(request, 'fromagerie/contact.html', {'form': form})

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

def intranet(request):
    return render(request, 'fromagerie/intranet.html')

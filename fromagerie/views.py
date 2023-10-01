from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContactFormModel
from .models import Producto
from .forms import ProductoForm
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

# CRUD PRODUCTOS
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'fromagerie/lista_productos.html', {'productos': productos})
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ProductoForm()
    return render(request, 'fromagerie/crear_producto.html', {'form': form})
@login_required
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'fromagerie/actualizar_producto.html', {'form': form, 'producto': producto})
@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('shop')
    
    return render(request, 'fromagerie/eliminar_producto.html', {'producto': producto})
# FIN CRUD PRODUCTOS

def login(request):
    return render(request, 'fromagerie/login.html')
def signup(request):
    return render(request, 'fromagerie/signup.html')
def recoverpassword(request):
    return render(request, 'fromagerie/recoverpassword.html')
def about(request):
    return render(request, 'fromagerie/about.html')


def shop(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'fromagerie/shop.html', data)


def carrito(request):
    return render(request, 'fromagerie/carrito.html')
def intranet(request):
    return render(request, 'fromagerie/intranet.html')

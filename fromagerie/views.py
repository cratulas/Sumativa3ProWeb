from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContactFormModel
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import user_passes_test
from .permissions import es_admin
from django.contrib import messages
from rest_framework import viewsets
from .serializers import ProductoSerializer
import requests
from django.http import JsonResponse

def cheese_list(request):
    response = requests.get("https://cheese-api.onrender.com/cheeses")
    cheeses = response.json() if response.status_code == 200 else []
    
    return render(request, "fromagerie/cheese_list.html", {"cheeses": cheeses})

def obtener_cheeses(request):
    url = "https://cheese-api.onrender.com/cheeses"
    
    response = requests.get(url)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "No se pudo obtener la información de la API"}, status=500)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        return productos

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
@user_passes_test(es_admin, login_url='/admin/')
def lista_productos(request):
    # Comprueba si el usuario tiene permisos y, si no, agrega un mensaje de error.
    if not es_admin(request.user):
        messages.error(request, 'Debes estar logeado como administrador para acceder a esta página.')
        return redirect('admin')
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

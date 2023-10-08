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
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from .forms import UpdateProfileForm, ChangePasswordForm

from .models import Producto, Carrito, ItemCarrito


@login_required
def add_to_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('carrito')

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.get(user=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)

    for item in items:
        item.subtotal = item.cantidad * item.producto.precio

    return render(request, 'fromagerie/carrito.html', {'items': items})


@login_required
def eliminar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__user=request.user)
    item.delete()
    return redirect('carrito')

# Perfiles de usuario
@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateProfileForm(request.POST, instance=request.user)
        password_form = ChangePasswordForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect('index')
    else:
        user_form = UpdateProfileForm(instance=request.user)
        password_form = ChangePasswordForm(request.user)
    
    return render(request, 'fromagerie/update_profile.html', {'user_form': user_form, 'password_form': password_form})

def logout_view(request):
    logout(request)
    return redirect('index') 

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'login_successful')
            return redirect('index')
        else:
            messages.error(request, 'Username o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'fromagerie/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'fromagerie/signup.html', {'form': form})

# FIN PERFILES DE USUARIO


# CONSUMO DE API Y RESPUESTA COMO html
def cheese_list(request):
    response = requests.get("https://cheese-api.onrender.com/cheeses")
    cheeses = response.json() if response.status_code == 200 else []
    
    return render(request, "fromagerie/cheese_list.html", {"cheeses": cheeses})

# CONSUMO DE API Y RESPUESTA COMO json
def obtener_cheeses(request):
    url = "https://cheese-api.onrender.com/cheeses"
    
    response = requests.get(url)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "No se pudo obtener la información de la API"}, status=500)


# API PROPIA
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


#####################################
# CRUD PRODUCTOS
@user_passes_test(es_admin, login_url='/admin/')
def lista_productos(request):
    # Comprueba si el usuario tiene permisos y, si no, agrega un mensaje de error.
    if not es_admin(request.user):
        messages.error(request, 'Debes estar logeado como administrador para acceder a esta página.')
        return redirect('admin')
    productos = Producto.objects.all()
    return render(request, 'fromagerie/lista_productos.html', {'productos': productos})
@user_passes_test(es_admin, login_url='/admin/')
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ProductoForm()
    return render(request, 'fromagerie/crear_producto.html', {'form': form})
@user_passes_test(es_admin, login_url='/admin/')
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
@user_passes_test(es_admin, login_url='/admin/')
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('shop')
    
    return render(request, 'fromagerie/eliminar_producto.html', {'producto': producto})
# FIN CRUD PRODUCTOS
###################################

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

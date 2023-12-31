from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
# from .views import index,contact
# path('',index,name='index'),
# path('contact/',contact,name='contact'),

router = routers.DefaultRouter()
router.register(r'producto', views.ProductoViewSet)
#localhost:8000/api/producto

urlpatterns = [
    path('', views.index,name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('about/', views.about,name='about'),
    path('shop/', views.shop, name='shop'),
    path('add_to_carrito/<int:producto_id>/', views.add_to_carrito, name='add_to_carrito'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('eliminar_item/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.actualizar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('api/v1/', include(router.urls)),
    path("cheeses/", views.cheese_list, name="cheese_list"), #html
    path('cheeses/json', views.obtener_cheeses, name='obtener_cheeses'), #jsON
    ]



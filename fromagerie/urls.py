from django.urls import path
from . import views
# from .views import index,contact
# path('',index,name='index'),
# path('contact/',contact,name='contact'),

urlpatterns = [
    path('', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('recoverpassword/', views.recoverpassword,name='recoverpassword'),
    path('about/', views.about,name='about'),
    path('shop/', views.shop, name='shop'),
    path('carrito/', views.carrito, name='carrito'),
    path('intranet/', views.intranet, name='intranet'),
    ]

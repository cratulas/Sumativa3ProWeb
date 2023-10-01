from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre


class ContactForm(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    asunto = models.CharField(max_length=200, blank=False)
    mensaje = models.TextField(blank=False)
    
    def __str__(self):
        return self.nombre
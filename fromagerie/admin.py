from django.contrib import admin
from .models import ContactForm, Producto
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "precio", "stock"]
    list_editable = ["descripcion", "precio"]
    search_fields = ["nombre"]

admin.site.register(ContactForm)
admin.site.register(Producto, ProductoAdmin)
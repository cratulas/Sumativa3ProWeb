from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    
    def validate_nombre(self, value):
        exis = Producto.objects.filter(nombre=value).exists()

        if exis:
            raise serializers.ValidationError("Este producto ya existe")

    class Meta:
        model = Producto
        fields = '__all__'
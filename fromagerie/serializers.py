from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    
    def validate_nombre(self, value):

        instance = self.instance
        if instance:

            if instance.nombre == value:
                return value

        exis = Producto.objects.filter(nombre=value).exists()
        if exis:
            raise serializers.ValidationError("Este producto ya existe")
        return value

    class Meta:
        model = Producto
        fields = '__all__'
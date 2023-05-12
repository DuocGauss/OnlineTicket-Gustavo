from rest_framework import serializers
from .models import Arriendo

class srlzProducto(serializers.ModelSerializer):
    
    class Meta:
        model=Arriendo
        fields=["id","nombre_est","descripcion","valor","estado","imagen"]
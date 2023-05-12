from django.contrib import admin
from .models import Arriendo, Pedido, Persona

# Register your models here.
class AdmPersona(admin.ModelAdmin):
    list_display=["rut","nombre","correo","contraseña"]
    list_filter=["nombre","correo"]
    list_editable=["nombre","correo"]

    class Meta:
        model=Persona

class AdmArriendo(admin.ModelAdmin):
    list_display=["id","nombre_est","descripcion","estado","imagen"]
    list_filter=["nombre_est","estado"]
    list_editable=["nombre_est","descripcion","estado","imagen"]
    
    class Meta:
        model=Arriendo


class AdmPedido(admin.ModelAdmin):
    list_display=["id","rut","nombrecli","direccion","comuna","telefono","estado"]
   
    class Meta:
        model=Pedido       

admin.site.register(Persona, AdmPersona)
admin.site.register(Arriendo, AdmArriendo)
admin.site.register(Pedido, AdmPedido)
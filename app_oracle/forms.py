from django.forms import fields
from app_oracle.models import Arriendo, Pedido
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class frmCrearUsuario(UserCreationForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=["username","first_name","last_name","email","password1","password2"]

class frmModificarUsuario(UserChangeForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"] 
            

class frmArriendo(forms.ModelForm):
    class Meta:
        model=Arriendo
        fields=["id","nombre_est","descripcion","valor","estado","imagen"]


class frmCompra(forms.ModelForm):
    class Meta:
        model=Pedido
        fields=["id","rut","nombrecli","direccion","comuna","telefono"]

class frmEstado(forms.ModelForm):
    class Meta:
        model=Pedido
        fields=["estado"]        

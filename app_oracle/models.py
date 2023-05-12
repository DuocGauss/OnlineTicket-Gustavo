from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=50)
    correo=models.CharField(max_length=25)
    contraseña=models.CharField(max_length=25,default=".")

def __str__(self):
    return self.rut


class Arriendo(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    nombre_est=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    valor=models.IntegerField(default=0)
    estado=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to="imgprod",null=True)

def __str__(self):
    return self.id  + "  " + self.nombre_est 


class MiCarrito(models.Model):
    cliente=models.CharField(max_length=50,null=False)
    producto=models.CharField(max_length=50,null=False)
    valor=models.IntegerField(default=0) 

class Pedido(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    rut=models.CharField(max_length=10)   
    nombrecli=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    comuna=models.CharField(max_length=50)
    telefono=models.IntegerField(default=0)
    estado=models.CharField(max_length=50) 
    
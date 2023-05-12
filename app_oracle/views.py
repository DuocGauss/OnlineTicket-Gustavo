from django.contrib.auth.models import User
from .forms import frmArriendo, frmCompra, frmCrearUsuario, frmEstado, frmModificarUsuario
from .models import Arriendo, Pedido, Persona, MiCarrito
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from rest_framework import viewsets
from .serializers import srlzProducto
from django.contrib.auth import get_user
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Arriendo.objects.all()
    serializer_class=srlzProducto


# Create your views here.
def intex(request):
    prods=Arriendo.objects.all()
    contexto={
        "productos":prods,
    }
    
    return render(request,"app_oracle/intex.html",contexto)   

def intexusuario(request):
    prods=Arriendo.objects.all()
    contexto={
        "productos":prods,
    }
    
    return render(request,"app_oracle/intexusuario.html",contexto)   

def productos_adm(request):
    msg="Listado De Arriendos"
    Productos=Arriendo.objects.all()
    contexto={
        "mensaje":msg,
        "Productos":Productos
    }
    return render(request,"app_oracle/productos_adm.html",contexto)   


def administrarusuarios(request):
    people=User.objects.all()

    contexto={
        "lista":people
    }

    return render(request,"app_oracle/administrarusuarios.html", contexto)     


def agregarproducto(request):
    form=frmArriendo(request.POST or None)
    
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=frmArriendo(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"Arriendo Publicado!")

           return redirect(to="intexusuario")
        
    

    return render(request,"app_oracle/agregarproducto.html",contexto)


def modificarprod(request,id):
    prod=get_object_or_404(Arriendo,id=id)
    form=frmArriendo(instance=prod)
    #form.fields["id"].disabled=True
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=frmArriendo(data=request.POST,files=request.FILES,instance=prod)
        #form.fields["id"].disabled=False
        if form.is_valid():
            prod_buscado=Arriendo.objects.get(id=prod.id)
            datos_form=form.cleaned_data
            prod_buscado.nombre_est=datos_form.get("nombre_est")
            prod_buscado.descripcion=datos_form.get("descripcion")
            prod_buscado.valor=datos_form.get("valor")
            prod_buscado.estado=datos_form.get("estado")
            prod_buscado.imagen=datos_form.get("imagen")
            prod_buscado.save()
            messages.success(request,"Arriendo Modificado")
            return redirect(to="productos_adm")
        contexto["form"]=form
        
    return render(request,"app_oracle/modificarprod.html",contexto)


def eliminarprod(request,id):
    prod=get_object_or_404(Arriendo,id=id)
    #info=f"ID:{prod.id} MARCA:{prod.marca} {prod.descripcion}"

    contexto={

        #"info":info
        "producto":prod
    }
    
    if request.method=="POST":
        prod.delete()
        messages.success(request,"Arriendo eliminado correctamente")
        return redirect(to="productos_adm")

    return render(request,"app_oracle/eliminarprod.html",contexto) 

def productos(request):
    prods=Arriendo.objects.all()
    contexto={
        "productos":prods,
    }
    
    if request.user.is_authenticated:
        cant=MiCarrito.objects.filter(cliente=request.user.username).count()
    contexto={
        "productos":prods,
        "cuenta":cant,
    }
    


    return render(request,"app_oracle/productos.html",contexto)   


def CambiarContraseña(request):
    if request.method=="POST":
        
        form = PasswordChangeForm(request.user, request.POST)
        old_password=request.POST.get("old_password")
        new_password1=request.POST.get("new_password1")
        new_password2=request.POST.get("new_password2")
        if not check_password(old_password, request.user.password):
            messages.error(request,"Su contraseña actual no coincide")
            return redirect(to=CambiarContraseña)
        if new_password1!=new_password2:
            messages.error(request,"Las contraseñas no coinciden")
            return redirect(to=CambiarContraseña)
        if form.is_valid():
            update_session_auth_hash(request, form.save())
            messages.success(request,"Su contraseña fue actualizada exitosamente")
            return redirect(to=GestionUsuario)
    form=PasswordChangeForm(request.user)
    contexto={
    "form":form
    }
    return render(request, "app_lmgas/CambiarContraseña.html",contexto)

def administrador(request):
    return render(request, "app_oracle/administrador.html")   

def pedidos(request):
    Pedidos=Pedido.objects.all()
    contexto={
        "Pedidos":Pedidos
    }
    
    return render(request, "app_oracle/pedidos.html",contexto)
    

def RecuperCuenta(request):
    return render(request, "app_oracle/RecuperCuenta.html") 

def RecuperCuenta2(request):
    return render(request, "app_oracle/RecuperCuenta2.html")   

def RecuperCuenta3(request):
    return render(request, "app_oracle/RecuperCuenta3.html") 


def GestionUsuario(request):
    context = {}
    check = User.objects.filter(pk=request.user.pk)
    if len(check)>0:
        data = User.objects.get(pk=request.user.pk)
        context["data"] = data
    return render(request,"app_oracle/GestionUsuario.html",context)
    

def crearcuenta(request):
    form=frmCrearUsuario()
    if request.method=="POST":
        form=frmCrearUsuario(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Gracias por registrarte")
            return redirect(to="intex")

    contexto={
        "form":form
    }
    return render(request, "registration/crearcuenta.html",contexto)  



def Ordendecompra(request):
    Pedidos=Pedido.objects.all()
    contexto={
        "Pedidos":Pedidos
    }
    return render(request,"app_oracle/Ordendecompra.html",contexto)   
    




def modificaruser(request,id):
    us=get_object_or_404(User,id=id)
    form=frmModificarUsuario(instance=us)
    #form.fields["id"].disabled=True
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=frmModificarUsuario(data=request.POST,files=request.FILES,instance=us)
        #form.fields["id"].disabled=False
        if form.is_valid():
            us_buscado=User.objects.get(id=us.id)
            datos_form=form.cleaned_data
            us_buscado.username=datos_form.get("username")
            us_buscado.first_name=datos_form.get("first_name")
            us_buscado.last_name=datos_form.get("last_name")
            us_buscado.email=datos_form.get("email")
            us_buscado.save()
            messages.success(request,"Usuario Modificado")
            return redirect(to="GestionUsuario")
        contexto["form"]=form
        
    return render(request,"app_oracle/modificaruser.html",contexto) 


def carrito(request):
    car=MiCarrito.objects.all()
    contexto={
        "carrito":car,
    }
    return render(request, "app_oracle/carrito.html",contexto) 

def confirmacionprod(request):
    if request.user.is_authenticated:
        return render(request, "app_oracle/confirmacionprod.html")
    else:
        return redirect(to="login")

def PagoProducto(request):
    Compra=Pedido.objects.all()
    contexto={
        "compra":Compra
    }
    return render(request,"app_oracle/PagoProducto.html",contexto)   

def agregarcarrito(request,id,valor ):
    
    if request.user.is_authenticated:
        car=MiCarrito()
        car.cliente=request.user.username
        car.producto=id
        car.valor=valor
        car.save()
        messages.success(request,"Producto agregado al carrito")
        return redirect(to="productos")


def eliminarcar(request, id):
    car=get_object_or_404(MiCarrito,id=id)
    #info=f"ID:{prod.id} MARCA:{prod.marca} {prod.descripcion}"

    contexto={

        #"info":info
        "car":car
    }
    
    if request.method=="POST":
        car.delete()
        messages.success(request,"Producto eliminado del carrito")
        return redirect(to="carrito")

    return render(request,"app_oracle/eliminarcar.html",contexto)


def agregarcompra(request):
    form=frmCompra(request.POST or None)
    
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=frmCompra(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"Compra realizada!")

           return redirect(to="productos")
        
    

    return render(request,"app_oracle/agregarcompra.html",contexto)



def modificarped(request,id):
    ped=get_object_or_404(Pedido,id=id)
    form=frmEstado(instance=ped)
    #form.fields["id"].disabled=True
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=frmEstado(data=request.POST,files=request.FILES,instance=ped)
        #form.fields["id"].disabled=False
        if form.is_valid():
            prod_buscado=Pedido.objects.get(id=ped.id)
            datos_form=form.cleaned_data
            prod_buscado.estado=datos_form.get("estado")
            prod_buscado.save()
            messages.success(request,"Pedido Modificado")
            return redirect(to="pedidos")
        contexto["form"]=form
        
    return render(request,"app_oracle/modificarped.html",contexto)


def eliminarped(request,id):
    ped=get_object_or_404(Pedido,id=id)
    #info=f"ID:{prod.id} MARCA:{prod.marca} {prod.descripcion}"

    contexto={

        #"info":info
        "ped":ped
    }
    
    if request.method=="POST":
        ped.delete()
        messages.success(request,"Pedido eliminado correctamente")
        return redirect(to="pedidos")

    return render(request,"app_oracle/eliminarped.html",contexto)


def arriendo_user(request):
    msg="Listado De Arriendos"
    Productos=Arriendo.objects.all()
    contexto={
        "mensaje":msg,
        "Productos":Productos
    }
    return render(request,"app_oracle/arriendo_user.html",contexto)   
 


def mod_arriendo(request,id):
    prod=get_object_or_404(Arriendo,id=id)
    form=frmArriendo(instance=prod)
    #form.fields["id"].disabled=True
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=frmArriendo(data=request.POST,files=request.FILES,instance=prod)
        #form.fields["id"].disabled=False
        if form.is_valid():
            prod_buscado=Arriendo.objects.get(id=prod.id)
            datos_form=form.cleaned_data
            prod_buscado.nombre_est=datos_form.get("nombre_est")
            prod_buscado.descripcion=datos_form.get("descripcion")
            prod_buscado.valor=datos_form.get("valor")
            prod_buscado.estado=datos_form.get("estado")
            prod_buscado.imagen=datos_form.get("imagen")
            prod_buscado.save()
            messages.success(request,"Arriendo Modificado")
            return redirect(to="arriendo_user")
        contexto["form"]=form
        
    return render(request,"app_oracle/mod_arriendo.html",contexto)


def eliminar_arriendo(request,id):
    prod=get_object_or_404(Arriendo,id=id)
    #info=f"ID:{prod.id} MARCA:{prod.marca} {prod.descripcion}"

    contexto={

        #"info":info
        "producto":prod
    }
    
    if request.method=="POST":
        prod.delete()
        messages.success(request,"Arriendo eliminado correctamente")
        return redirect(to="arriendo_user")

    return render(request,"app_oracle/eliminar_arriendo.html",contexto) 

def confirmar(request, id):
    if request.user.is_authenticated:
        prods = Arriendo.objects.get(id=id)
        return render(request, "app_oracle/confirmar.html", {'prods':prods})
    else:
        return redirect(to="login")
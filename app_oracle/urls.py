from django.db import router
from django.urls import path, include
from .views import GestionUsuario, Ordendecompra, CambiarContraseña, PagoProducto, RecuperCuenta, RecuperCuenta2, RecuperCuenta3, administrador, agregarcompra, agregarproducto, arriendo_user, carrito, confirmacionprod, crearcuenta, eliminar_arriendo, eliminarcar, eliminarped, eliminarprod, intex, intexusuario, mod_arriendo, modificarped, modificarprod, modificaruser, pedidos, productos, productos_adm, administrarusuarios, ProductoViewSet, agregarcarrito, confirmar
from rest_framework import routers

router=routers.DefaultRouter()
router.register('arriendos', ProductoViewSet)

urlpatterns = [
    path('',intex,name="intex"),
    path('productos_adm/',productos_adm,name="productos_adm"),
    path('administrarusuarios/',administrarusuarios,name="administrarusuarios"),
    path('agregarproducto/',agregarproducto, name="agregarproducto"),
    path('modificarprod/<id>',modificarprod, name="modificarprod"),
    path('eliminarprod/<id>',eliminarprod, name="eliminarprod"),
    path('productos/',productos, name="productos"),
    path('intexusuario/',intexusuario, name='intexusuario'),
    path('administrador/',administrador, name='administrador'),
    path('pedidos/',pedidos, name='pedidos'),
    path('RecuperCuenta/',RecuperCuenta, name='RecuperCuenta'),
    path('RecuperCuenta2/',RecuperCuenta2, name='RecuperCuenta2'),
    path('RecuperCuenta3/',RecuperCuenta3, name='RecuperCuenta3'),
    path('GestionUsuario/',GestionUsuario, name='GestionUsuario'),
    path('crearcuenta/',crearcuenta, name='crearcuenta'),
    path('Ordendecompra/',Ordendecompra, name='Ordendecompra'),
    path('modificaruser/<id>',modificaruser, name='modificaruser'),
    path('carrito/',carrito, name='carrito'),
    path('confirmacionprod/',confirmacionprod, name='confirmacionprod'),
    path('PagoProducto/',PagoProducto, name='PagoProducto'),
    path('api/',include(router.urls)),
    path('agregarcarrito/<id> <valor>',agregarcarrito, name='agregarcarrito'),
    path('eliminarcar/<id>',eliminarcar, name="eliminarcar"),
    path('agregarcompra/',agregarcompra, name="agregarcompra"),
    path('modificarped/<id>',modificarped, name="modificarped"),
    path('eliminarped/<id>', eliminarped, name="eliminarped"),
    path('CambiarContraseña/', CambiarContraseña,name="CambiarContraseña"),
    path('arriendo_user/', arriendo_user,name="arriendo_user"),
    path('mod_arriendo/<id>',mod_arriendo, name="mod_arriendo"),
    path('eliminar_arriendo/<id>',eliminar_arriendo, name="eliminar_arriendo"),
    path('confirmar/<int:id>',confirmar, name='confirmar'),
]
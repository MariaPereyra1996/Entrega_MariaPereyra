from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name= "inicio"),
    path('Inicio/',Inicio, name= "Inicio"),
    path('Nosotros/',Nosotros, name= "Nosotros"),
    path('servicios/',servicios, name= "servicios"),
    path('clientes/',clientes, name= "clientes"),
    path('suscripcionForm/',suscripcionForm, name= "suscripcionForm"),
    path('suscripcionForm2/',suscripcionForm2, name= "suscripcionForm2"),
    path('serviciosForm/',serviciosForm, name= "serviciosForm"),
    path('serviciosForm2/',serviciosForm2, name= "serviciosForm2"),
    path('clientesForm/',clientesForm, name= "clientesForm"),
    path('clientesForm2/',clientesForm2, name= "clientesForm2"),
    path('buscar_servicio/',buscarServicio, name= "buscar_servicio"),
    path('buscar2/',buscar2, name= "buscar2"),
]

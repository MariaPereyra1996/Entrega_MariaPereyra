from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import*

def index(request):
    return render(request,"aplicacion/Base.html")

def Inicio(request):
    return render(request,"aplicacion/Inicio.html")

def Nosotros(request):
    return render(request,"aplicacion/Nosotros.html")

def servicios(request):
    ctx= {"servicios":Servicios.objects.all()}
    return render(request,"aplicacion/servicios.html",ctx)

def clientes(request):
    ctx= {"clientes":Clientes.objects.all()}
    return render(request,"aplicacion/clientes.html",ctx)

def suscripcionForm(request): #Form para el Modelo de suscripciones
    if request.method== "POST":
        suscripcion= Suscripcion(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'] )
        suscripcion.save()
        return HttpResponse("Se datos fueron enviados correctamente")
    return render(request,"aplicacion/suscripcionForm.html")

def suscripcionForm2(request): #Form_2 para el Modelo de suscripciones
    if request.method== "POST":
        miform=Sus_Form(request.POST)
        print(miform)
        if miform.is_valid:
            informacion= miform.cleaned_data
            suscripcion=Suscripcion(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            suscripcion.save()
            return render(request,"aplicacion/Base.html")
    else:
        miform=Sus_Form()
       
    return render(request, "aplicacion/suscripcionForm2.html", {"Form":miform})

def serviciosForm(request): #Form para el Modelo de servicios
    if request.method== "POST":
        servicios= Servicios(nombre=request.POST['nombre'], encargado=request.POST['encargado'] )
        servicios.save()
        return HttpResponse("Se datos fueron enviados correctamente")
    return render(request,"aplicacion/serviciosForm.html")

def serviciosForm2(request): #Form_2 para el Modelo de servicios
    if request.method== "POST":
        miform_servicios=Ser_Form(request.POST)
        print(miform_servicios)
        if miform_servicios.is_valid:
            informacion_S= miform_servicios.cleaned_data
            servicios=Servicios(nombre=informacion_S['nombre'],encargado=informacion_S['encargado'],)
            servicios.save()
            return render(request,"aplicacion/Base.html")
    else:
        miform_servicios=Ser_Form()
       
    return render(request, "aplicacion/serviciosForm2.html", {"Form":miform_servicios})

def clientesForm(request): #Form para el Modelo de servicios
    if request.method== "POST":
        clientes= Clientes(nombre=request.POST['nombre'], servicio_contratado=request.POST['servicio_contratado'], email=request.POST['email'] )
        clientes.save()
        return HttpResponse("Se datos fueron enviados correctamente")
    return render(request,"aplicacion/clientesForm.html")

def clientesForm2(request): #Form_2 para el Modelo de servicios
    if request.method== "POST":
        miform_clientes=Cli_Form(request.POST)
        print(miform_clientes)
        if miform_clientes.is_valid:
            informacion_C= miform_clientes.cleaned_data
            clientes=Clientes(nombre=informacion_C['nombre'],servicio_contratado=informacion_C['servicio_contratado'],email=informacion_C['email'])
            clientes.save()
            return render(request,"aplicacion/Base.html")
    else:
        miform_clientes=Cli_Form()
       
    return render(request, "aplicacion/clientesForm2.html", {"Form":miform_clientes})

def buscarServicio(request):
    return render(request,"aplicacion/buscarServicio.html")

def buscar2(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        encargado= Servicios.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadosServicios.html", {"nombre":nombre, "encargado":encargado})
    return HttpResponse("No se encuentra ese servicio")
        



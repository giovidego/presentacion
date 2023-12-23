from django.shortcuts import render


# Create your views here.

def inicio(request):
    context = {}
    return render(request,"inicio.html" ,context)

def contacto(request):
    context={}
    return render(request,"contacto.html",context)

def catalogo(request):
    context={}
    return render(request, "catalogo.html",context)

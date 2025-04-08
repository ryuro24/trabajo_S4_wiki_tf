from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'menuprincipal_wiki.html')

def forowiki(request):
    return render(request, 'forowiki.html')  # Replace 'foro.html' with the actual template you want to render

def registrarse_wiki(request):
    return render(request, 'registrarse_wiki.html')  # Replace 'registrarse.html' with the actual template

def inicio_sesion_wiki(request):
    return render(request, 'inicio_sesion_wiki.html')  # Replace 'login.html' with the actual template

def micuentatf(request):
    return render(request, 'micuentatf.html')

def Animales(request):
    return render(request, 'Animales.html')

def lugarestf(request):
    return render(request, 'Lugarestf.html')

def Enemigos(request):
    return render(request, 'Enemigos.html')

def Construcciones(request):
    return render(request, 'Construcciones.html')

def Flora(request):
    return render(request, 'Flora.html')

def Armas(request):
    return render(request, 'Armas.html')

def Consumibles(request):
    return render(request, 'Consumibles.html')

def historia(request):
    return render(request, 'historia.html')

def Logros(request):
    return render(request, 'Logros.html')
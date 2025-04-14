from django.shortcuts import render, redirect
from apptest.forms import RegistroUsuarioForm, LoginForm
from apptest.models import Rol,Usuario
from .forms import EditarUsuarioForm
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'menuprincipal_wiki.html')

def forowiki(request):
    usuario_email = request.session.get('usuario_email')
    if not usuario_email:
        return redirect('inicio_sesion_wiki')  # No está logueado

    return render(request, 'forowiki.html', {'usuario_email': usuario_email})

def registrarse_wiki(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)

            # Busca el rol "usuario" y se lo asigna
            try:
                rol_usuario = Rol.objects.get(nombre__iexact="usuario")
                usuario.rol = rol_usuario
            except Rol.DoesNotExist:
                # Si no existe, podrías crear uno o lanzar error
                rol_usuario = Rol.objects.create(nombre="usuario")
                usuario.rol = rol_usuario

            usuario.save()
            return redirect('inicio')  # O a donde quieras redirigir
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registrarse_wiki.html', {'form': form})

def inicio_sesion_wiki(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            contrasena = form.cleaned_data['contrasena']
            usuario = Usuario.objects.get(email=email)

            # Guardamos el ID del usuario en la sesión
            request.session['usuario_id'] = usuario.id
            request.session['usuario_email'] = usuario.email
            request.session['usuario_rol'] = usuario.rol.nombre if usuario.rol else 'Sin Rol'

            return redirect('inicio')
    else:
        form = LoginForm()

    return render(request, 'inicio_sesion_wiki.html', {
        'form': form
    })

def micuentatf(request):
    if 'usuario_email' not in request.session:
        return redirect('inicio_sesion_wiki')

    email_actual = request.session['usuario_email']
    try:
        usuario = Usuario.objects.get(email=email_actual)
    except Usuario.DoesNotExist:
        return redirect('inicio_sesion_wiki')

    form = EditarUsuarioForm(instance=usuario)

    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Actualiza la sesión si el email cambia
            request.session['usuario_email'] = form.cleaned_data['email'].lower()
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect('micuentatf')

    # Masked password by default for display purposes
    usuario_contrasena = '********'  # Masked password by default
    return render(request, 'micuentatf.html', {
        'usuario_email': usuario.email,
        'form': form,
        'usuario_contrasena': usuario.contrasena,  # Send the actual password for toggling
    })

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

def cerrar_sesion(request):
    try:
        del request.session['usuario_email']
    except KeyError:
        pass

    return redirect('inicio')
from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm


# Create your views here.

def index(request):
    return render (request,'aplicacion1/index.html')

def contacto(request):
    return render (request,'aplicacion1/contacto.html')

def productos(request):
    return render (request,'aplicacion1/productos.html')

def usuarios(request):
    usuario=Usuario.objects.all()
    return render (request,'aplicacion1/usuarios.html',{"data":usuario})

def ejemplo(request):
    return render (request,'aplicacion1/ejemplo.html')

def  formulario_usuario(request):

    form = UsuarioForm()
    
    if request.method == "POST":
        form=UsuarioForm(data=request.POST)

        if form.is_valid():
            usuario=Usuario()
            usuario.rut=form.cleaned_data['rut']
            usuario.nombre=form.cleaned_data['nombre']
            usuario.apellido=form.cleaned_data['apellido']
            usuario.edad=form.cleaned_data['edad']
            usuario.email=form.cleaned_data['email']
            usuario.save()

        return redirect('/usuarios')
    else:
        form = UsuarioForm()
        return render (request, 'aplicacion1/formulario_usuario.html',{"form":form})


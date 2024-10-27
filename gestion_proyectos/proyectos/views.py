from django.shortcuts import render, redirect
from .models import Usuario, Equipo, Proyecto, Tarea
from .forms import UsuarioForm, EquipoForm, ProyectoForm, TareaForm

# Create your views here.

def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'proyectos/usuario_form.html', {'form': form})

def crear_equipo(request):
    form = EquipoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_equipos')
    return render(request, 'proyectos/equipo_form.html', {'form': form})

def crear_proyecto(request):
    form = ProyectoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_proyectos')
    return render(request, 'proyectos/proyecto_form.html', {'form': form})

def crear_tarea(request):
    form = TareaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_tareas')
    return render(request, 'proyectos/tarea_form.html', {'form': form})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # O lo que necesites
    return render(request, 'proyectos/lista_usuarios.html', {'usuarios': usuarios})

def lista_equipos(request):
    equipos = Equipo.objects.all()  # Obtén todos los equipos
    return render(request, 'proyectos/lista_equipos.html', {'equipos': equipos})

def lista_tareas(request):
    Tareas = Tarea.objects.all()  # Obtén todos los equipos
    return render(request, 'proyectos/lista_equipos.html', {'equipos': Tareas})

def lista_proyectos(request):
    Proyectos = Proyecto.objects.all()  # Obtén todos los equipos
    return render(request, 'proyectos/lista_equipos.html', {'equipos': Proyectos})

def pagina_principal(request):
    return render(request, 'proyectos/pagina_principal.html')
from django import forms
from .models import Usuario, Equipo, Proyecto, Tarea

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'rol',]  

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre']  

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'tipo', 'equipos']  

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion', 'inicio', 'termino', 'responsable', 'ejecutor', 'proyecto']

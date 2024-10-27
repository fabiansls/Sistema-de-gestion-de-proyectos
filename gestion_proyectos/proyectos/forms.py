from django import forms
from .models import Usuario, Equipo, Proyecto, Tarea

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'rol',]  # Ajusta los campos según tu modelo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre']  # Ajusta los campos según tu modelo

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'tipo', 'equipos']  # Ajusta los campos según tu modelo

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion', 'inicio', 'termino', 'responsable', 'ejecutor', 'proyecto']

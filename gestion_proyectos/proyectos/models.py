from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, choices=[("Responsable", "Responsable"), ("Ejecutor", "Ejecutor")])

    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    usuarios = models.ManyToManyField(Usuario, related_name='equipos')

    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[("Individual", "Individual"), ("En equipo", "En equipo")])
    equipos = models.ManyToManyField(Equipo, related_name='proyectos', blank=True)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    inicio = models.DateField()
    termino = models.DateField()
    responsable = models.ForeignKey(Usuario, related_name='tareas_responsable', on_delete=models.SET_NULL, null=True)
    ejecutor = models.ForeignKey(Usuario, related_name='tareas_ejecutor', on_delete=models.SET_NULL, null=True)
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
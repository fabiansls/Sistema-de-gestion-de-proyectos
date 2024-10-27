from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('usuario/crear/', views.crear_usuario, name='crear_usuario'),
    path('equipo/crear/', views.crear_equipo, name='crear_equipo'),
    path('proyecto/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('tarea/crear/', views.crear_tarea, name='crear_tarea'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('equipo/lista/', views.lista_equipos, name='lista_equipos'),
    path('tarea/lista/', views.lista_tareas, name='lista_tareas'),
    path('proyecto/lista/', views.lista_proyectos, name='lista_proyectos'),
]

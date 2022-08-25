from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

app_name = "persona_app"

urlpatterns = [
        path(
        '', 
        views.InicioView.as_view(), 
        name='inicio',
        ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(), 
        name='lista_empleado'
        ),

    path(
        'lista-admin-empleados/', 
        views.ListAdminEmpleados.as_view(), 
        name='admin_empleado'
        ),

    path(
        'lista-by-area/<shortname>/', 
        views.ListByAreaEmpleado.as_view(),
        name='lista_area'
        ),
    
    path(
        'lista-by-trabajo/', 
        views.ListByTrabajoEmpleado.as_view(), 
        name='lista_trabajo'
        ), 
    
    path(
        'buscar-empleado/', 
        views.ListEmpleadosByKword.as_view(), 
        name='buscar-empleado'
        ), 
    
    path(
        'lista-habilidades-empleado/', 
        views.ListHabilidadesEmpleado.as_view(), 
        name='lista-habilidades'
        ),
    
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(), 
        name='ver_empleado'
        ),
    
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(), 
        name='añadir'
        ),
    
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
        ),

    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



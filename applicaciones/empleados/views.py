from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
    
)

#models
from .models import Empleado, Habilidades
#forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'empleados/lista_todos.html'
    paginate_by = 4
    ordering = 'id'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            nombre_completo__icontains=palabra_clave
        )
        return lista


class ListAdminEmpleados(ListView):
    template_name = 'empleados/lista_admin.html'
    paginate_by = 10
    ordering = 'id'
    context_object_name = 'empleados'
    model = Empleado
    
    
class ListByAreaEmpleado(ListView):
    """ Lista empleados por área"""
    template_name = 'empleados/lista_by_area.html'
    context_object_name = 'empleados' 
    ordering = 'nombre'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista
    

class ListByTrabajoEmpleado(ListView):
    """ Lista empleados por trabajo"""
    template_name = 'empleados/lista_by_trabajo.html'
    context_object_name = 'empleados'
    ordering = 'id'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista_trabajo = Empleado.objects.filter(
        trabajo=palabra_clave
        )
        return lista_trabajo      

class ListEmpleadosByKword(ListView)          :
    """ Lista empleado por palabra clave"""
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            primer_nombre=palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    """ Lista habilidades de un empleado"""
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id = self.request.GET.get("kword", '')
        empleado = Empleado.objects.get(id=id)
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context   
 
class EmpleadoCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:lista_empleado')

    def form_valid(self, form):
        #Lógica del proceso
        trabajador = form.save(commit=False)
        trabajador.nombre_completo = trabajador.primer_nombre + ' ' + trabajador.primer_apellido
        trabajador.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    fields = [
        'primer_nombre',
        'primer_apellido',
        'trabajo',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url = reverse_lazy('persona_app:admin_empleado')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST['primer_apellido'])
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"

    success_url = reverse_lazy('persona_app:lista_empleado')

# 1. - Lista todos los empleados de la empresa
# 2. - Listar todos los empleados que pertenecen a un area de la empresa
# 3. - Listar empleados por trabajo
# 4. - Listar los empleados por palabra clave
# 5. - Listar habilidades de un empleado

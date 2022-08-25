from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import(
    FormView
)
from applicaciones.empleados.models import Empleado

from .models import Departamento
from .forms import NewDepartamentoForm


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista_Departamento.html"
    context_object_name = 'departamentos'
    


class NewRegisterDepartamento(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        department=Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname'],
        )
        department.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            primer_nombre=nombre,
            primer_apellido=apellido,
            trabajo='1',
            departamento=department
        )
        return super(NewRegisterDepartamento, self).form_valid(form)

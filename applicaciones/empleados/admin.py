from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'primer_nombre',
        'primer_apellido',
        'departamento',
        'trabajo',
        'nombre_completo',
        'id',
    )

    #
    def nombre_completo(self, obj):
        return obj.primer_nombre + ' ' + obj.primer_apellido

    # Filtro Empleados
    search_fields = ('primer_nombre',)
    list_filter = ('departamento', 'trabajo', 'habilidades', 'nombre_completo' )

    # Filtro habilidades
    filter_horizontal = ('habilidades',)
    
admin.site.register(Empleado, EmpleadoAdmin)    

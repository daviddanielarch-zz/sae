from django.contrib import admin

from estudiantes.models import Estudiante, Historia, Tarea, Familiar


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'facultad')
    search_fields = ('nombre', )


class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'fecha_ultima_modificacion')
    search_fields = ('estudiante__nombre', )


class TareasAdmin(admin.ModelAdmin):
    list_filter = ('completada', )
    list_display = ('fecha_creacion', 'estudiante', 'datos', 'completada')


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Historia, HistoriaAdmin)
admin.site.register(Tarea, TareasAdmin)
admin.site.register(Familiar, FamiliarAdmin)

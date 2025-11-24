from django.contrib import admin

from apps.eventos.models import Evento

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'mostrar_voluntarios', 'fecha')
    search_fields = ('titulo',)
    list_filter = ('fecha', 'titulo')
    filter_horizontal = ('voluntarios',)  # Para mejor UX al asignar voluntarios
    
    def mostrar_voluntarios(self, obj):
        """Muestra la cantidad de voluntarios asignados"""
        count = obj.voluntarios.count()
        if count == 0:
            return "Sin voluntarios"
        elif count == 1:
            return "1 voluntario"
        else:
            return f"{count} voluntarios"
    
    mostrar_voluntarios.short_description = 'Voluntarios Asignados'
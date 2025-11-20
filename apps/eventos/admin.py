from django.contrib import admin

from apps.eventos.models import Evento

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'voluntarios', 'fecha')
    search_fields = ('titulo', 'voluntarios')
    list_filter = ('fecha', 'titulo')
    verbose_name = 'Evento'
    verbose_name_plural = 'Eventos'

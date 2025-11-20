from django.contrib import admin

from apps.voluntarios.models import Voluntario

# Register your models here.
@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_registro', 'email')

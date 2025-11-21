from django.urls import path
from apps.voluntarios import views

app_name = "voluntarios"

urlpatterns = [
    path("", views.lista_voluntarios, name="lista_voluntarios"),
    path("crear/", views.crear_voluntario, name="crear_voluntario"),
    path("editar/<int:id>/", views.editar_voluntario, name="editar_voluntario"),
    path("eliminar/<int:id>/", views.eliminar_voluntario, name="eliminar_voluntario"),
]

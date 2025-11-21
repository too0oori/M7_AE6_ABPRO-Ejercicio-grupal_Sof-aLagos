from django.urls import path

from apps.eventos import views

app_name = "eventos"


urlpatterns = [
    path("", views.lista_eventos, name="lista_eventos"),
    path("crear/", views.crear_evento, name="crear_evento"),
    path("editar/<int:id>/", views.editar_evento, name="editar_evento"),
    path("eliminar/<int:id>/", views.eliminar_evento, name="eliminar_evento"),
]
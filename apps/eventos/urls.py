from django.urls import path

from apps.eventos.views import index


app_name = "eventos"


urlpatterns = [
    path("", index, name="index"),
]

from django.urls import path

from apps.voluntarios.views import index

app_name = "voluntarios"


urlpatterns = [
    path("", index, name="index"),
]

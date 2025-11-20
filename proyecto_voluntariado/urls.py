from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include('apps.eventos.urls')),
    path('voluntarios/', include('apps.voluntarios.urls')),
]

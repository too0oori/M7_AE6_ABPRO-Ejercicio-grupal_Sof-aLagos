from django.shortcuts import render, redirect
from apps.eventos.models import Evento
from apps.eventos.forms import EventoForm
# Create your views here.
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'voluntarios/eventos_lista.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            return redirect('voluntarios:lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'voluntarios/crear_evento.html', {'form': form})

def editar_evento(request):
    evento = Evento.objects.get(id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('voluntarios:lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'voluntarios/editar_evento.html', {'form': form})

def eliminar_evento(request):
    evento = Evento.objects.get(id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('voluntarios:lista_eventos')
    return render(request, 'voluntarios/eliminar_evento.html', {'evento': evento})
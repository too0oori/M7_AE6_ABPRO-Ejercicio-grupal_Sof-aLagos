from django.shortcuts import render, redirect
from apps.voluntarios.models import Voluntario
from apps.voluntarios.forms import VoluntarioForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'voluntarios/lista_voluntarios.html', {'voluntarios': voluntarios})

@permission_required('voluntarios.add_voluntario')
def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            voluntario = form.save()
            return redirect('voluntarios:lista_voluntarios')
    else:
        form = VoluntarioForm()
    return render(request, 'voluntarios/formulario.html', {'form': form})

@permission_required('voluntarios.change_voluntario')
def editar_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('voluntarios:lista_voluntarios')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'voluntarios/formulario.html', {'form': form})

@permission_required('voluntarios.delete_voluntario')
def eliminar_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('voluntarios:lista_voluntarios')
    return render(request, 'voluntarios/eliminar_voluntario.html', {'voluntario': voluntario})

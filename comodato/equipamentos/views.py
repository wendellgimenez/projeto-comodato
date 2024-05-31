# equipamentos/views.py

from django.shortcuts import render, redirect
from .models import Equipamento
from .forms import EquipamentoForm

def equipamento_list(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/equipamento_list.html', {'equipamentos': equipamentos})

def equipamento_create(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamentos/equipamento_form.html', {'form': form})

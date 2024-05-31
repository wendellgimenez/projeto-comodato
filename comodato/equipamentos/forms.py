# equipamentos/forms.py

from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome_usuario', 'equipamento', 'modelo', 'patrimonio']

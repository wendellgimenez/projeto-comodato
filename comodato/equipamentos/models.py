# equipamentos/models.py

from django.db import models

class Equipamento(models.Model):
    nome_usuario = models.CharField(max_length=100)
    equipamento = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    patrimonio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome_usuario} - {self.equipamento}'

from django.db import models
from django.contrib.auth import get_user_model
from turmas.models import UsuarioTurma
# turma #

class Experimento(models.Model):
    nome = models.CharField(max_length=100)
    n_maquina = models.IntegerField()
    resultado = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=50)
    usuarioturma = models.ForeignKey(UsuarioTurma, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome
    




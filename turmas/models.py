from django.db import models
from django.contrib.auth import get_user_model
from usuario.models import Usuario


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, blank=True, null=True, unique=True)     
    matricula = models.ManyToManyField(Usuario, through='UsuarioTurma')

    def __str__(self):
        return self.nome
    

class UsuarioTurma(models.Model):
    data_matricula = models.DateField(auto_now_add=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
from django.db import models
from sistema.models import Experimento
from turmas.models import UsuarioTurma

class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    decricao = models.TextField()
   
    
    experimento = models.ForeignKey(Experimento,related_name='atividades', on_delete=models.CASCADE)
    responsavel = models.ForeignKey(UsuarioTurma,related_name='atividades', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo
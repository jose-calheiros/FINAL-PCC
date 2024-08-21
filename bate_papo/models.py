from django.db import models
from turmas.models import UsuarioTurma

class Bate_papo(models.Model):
    mensagem = models.CharField(max_length=300, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True) 
    usuarioturma = models.ForeignKey(UsuarioTurma, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.mensagem
    



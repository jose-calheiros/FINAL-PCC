from django.db import models
from django.contrib.auth import get_user_model
from usuario.models import Usuario
from atividades.models import Atividade
 

# turma #

class Comentarios(models.Model):
    texto = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    
    def __str__(self):
        return self.texto
    
  
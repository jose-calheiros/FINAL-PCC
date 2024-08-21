from django.contrib import admin
from .models import Atividade

class AtividadeAdmin(admin.ModelAdmin):
    
    def save(self):
        
        return self

admin.site.register(Atividade, AtividadeAdmin)
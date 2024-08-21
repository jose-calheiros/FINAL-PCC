from django.contrib import admin
from turmas.models import Turma

class TurmaAdmin(admin.ModelAdmin):

    def save(self):
        
        return self

admin.site.register(Turma, TurmaAdmin)
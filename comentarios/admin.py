from django.contrib import admin

from comentarios.models import Comentarios

class ComentariosAdmin(admin.ModelAdmin):
    
    def save(self):
        
        return self

admin.site.register(Comentarios, ComentariosAdmin)

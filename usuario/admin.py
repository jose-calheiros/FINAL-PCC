from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):

    def save(self):
        
        return self

admin.site.register(Usuario, UsuarioAdmin)
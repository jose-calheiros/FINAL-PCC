from django.contrib import admin
from .models import Bate_papo

class Bate_papoAdmin(admin.ModelAdmin):
    
    def save(self):
        
        return self

admin.site.register(Bate_papo, Bate_papoAdmin)
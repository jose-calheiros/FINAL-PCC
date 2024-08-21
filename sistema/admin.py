from django.contrib import admin
from .models import Experimento

class ExperimentoAdmin(admin.ModelAdmin):
    
    def save(self):
        
        return self

admin.site.register(Experimento, ExperimentoAdmin)
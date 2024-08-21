from django import forms
from .models import Turma

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'codigo']
       

class TurmaCodigoForm(forms.Form):
    codigo = forms.CharField(max_length=10, widget=forms.PasswordInput)

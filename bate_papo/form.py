from django import forms
from .models import Bate_papo


class Bate_papoForm(forms.ModelForm):
    class Meta:
        model = Bate_papo
        fields = ['mensagem']
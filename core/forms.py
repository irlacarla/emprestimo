from django import forms
from .models import CadastrarObjeto


class Notasforms(forms.ModelForm):
    class Meta:
        model = CadastrarObjeto
        fields = ("nome", "dono", "descricao")
        
        

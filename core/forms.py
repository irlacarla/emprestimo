from django import forms
from .models import CadastrarObjeto
from .forms import Notaforms


class Notasforms(forms.ModelForms):
    class Meta:
        model = CadastrarObjeto
        fields = ("texto", "texto", "texto")
        
        

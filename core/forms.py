from django import forms
from .models import Objeto
from .forms import CadastrarObjetoforms

class Notasforms(forms.ModelForms):
    class Meta:
        model = CadastrarObjeto
        fields = ("texto", "texto", "texto")
        
        

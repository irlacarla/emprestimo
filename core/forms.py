from django import forms
from .models import Objeto
from .forms import Notasforms

class Notasforms(forms.ModelForms):
    class Meta:
        model = Objeto
        fields = ("texto", "texto", "texto")
        
        

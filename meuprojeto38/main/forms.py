from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'ano_lancamento', 'onde_assistir', 'elenco']
        
        

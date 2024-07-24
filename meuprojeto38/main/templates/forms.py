from django import forms
from .models import Contato
from .models import Filme
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']



class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'ano_lancamento', 'diretor', 'sinopse']

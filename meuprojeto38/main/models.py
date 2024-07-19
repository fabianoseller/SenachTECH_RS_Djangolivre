# from django.db import models
# from .models import Filme

# from django import forms

# class FilmeTarantino(models.Model):
#     nome = models.CharField(max_length=255)
#     ano_lancamento = models.IntegerField()
#     onde_assistir = models.CharField(max_length=255)
#     elenco = models.TextField()

#     def __str__(self):
#         return self.nome




# class FilmeForm(forms.ModelForm):
#     class Meta:
#         model = Filme
#         fields = ['nome', 'ano_lancamento', 'onde_assistir', 'elenco']

from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    onde_assistir = models.CharField(max_length=100)
    elenco = models.TextField()

    def __str__(self):
        return self.nome


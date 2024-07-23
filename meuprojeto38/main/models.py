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
from django.contrib.auth.models import User

class Filme(models.Model):
    nome = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    onde_assistir = models.CharField(max_length=100)
    elenco = models.TextField()

    def __str__(self):
        return self.nome




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Cadastro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


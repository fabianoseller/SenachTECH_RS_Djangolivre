from django.db import models

# Create your models here.
from django.db import models

class FilmeTarantino(models.Model):
    nome = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    onde_assistir = models.CharField(max_length=255)
    elenco = models.TextField()

    def __str__(self):
        return self.nome

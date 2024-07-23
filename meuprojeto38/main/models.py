from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Filme(models.Model):
    nome = models.CharField(_("Nome"), max_length=100)
    ano_lancamento = models.IntegerField(_("Ano de Lançamento"))
    onde_assistir = models.CharField(_("Onde Assistir"), max_length=100)
    elenco = models.TextField(_("Elenco"))

    class Meta:
        verbose_name = _("Filme")
        verbose_name_plural = _("Filmes")
        ordering = ['-ano_lancamento', 'nome']

    def __str__(self):
        return f"{self.nome} ({self.ano_lancamento})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(_("Biografia"), max_length=500, blank=True)
    location = models.CharField(_("Localização"), max_length=30, blank=True)
    birth_date = models.DateField(_("Data de Nascimento"), null=True, blank=True)

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfis")

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Cadastro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cadastros')
    titulo = models.CharField(_("Título"), max_length=100)
    descricao = models.TextField(_("Descrição"))
    data_criacao = models.DateTimeField(_("Data de Criação"), auto_now_add=True)

    class Meta:
        verbose_name = _("Cadastro")
        verbose_name_plural = _("Cadastros")
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.titulo} - {self.user.username}"

class UserFilme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_filmes')
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='user_filmes')
    data_adicao = models.DateTimeField(_("Data de Adição"), auto_now_add=True)

    class Meta:
        verbose_name = _("Filme do Usuário")
        verbose_name_plural = _("Filmes dos Usuários")
        unique_together = ['user', 'filme']

    def __str__(self):
        return f"{self.user.username} - {self.filme.nome}"

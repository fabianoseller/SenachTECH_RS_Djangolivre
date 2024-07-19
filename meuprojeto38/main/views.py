from django.shortcuts import render, redirect
# from .forms import FilmeTarantinoForm
# from .views import cadastro_filme
from django.http import HttpResponseRedirect
from django.shortcuts import render
# def cadastro_filme(request):
#     if request.method == 'POST':
#         form = FilmeTarantinoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_filmes')  # Redireciona para uma página de lista de filmes
#     else:
#         form = FilmeTarantinoForm()
#     return render(request, 'cadastro_filme.html', {'form': form})

def index(request):
    return render(request, 'index.html')


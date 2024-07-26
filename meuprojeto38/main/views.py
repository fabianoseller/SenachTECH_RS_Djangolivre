from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, FilmeForm
from .models import Filme, Cadastro, Perfil
from django.db.models import Count

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('main:home')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    return render(request, 'main/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Você pode fazer login agora.')
            return redirect('main:login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def home_view(request):
    user_filmes = Cadastro.objects.filter(user=request.user).select_related('filme')
    return render(request, 'main/home.html', {'user_filmes': user_filmes})

@login_required
def add_filme_view(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            Cadastro.objects.create(user=request.user, filme=filme)
            messages.success(request, 'Filme adicionado com sucesso!')
            return redirect('main:home')
    else:
        form = FilmeForm()
    
    context = {
        'form': form,
    }
    return render(request, 'main/add_filme.html', context)

@login_required
def edit_filme_view(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme atualizado com sucesso!')
            return redirect('main:home')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'main/edit_filme.html', {'form': form, 'filme': filme})

@login_required
def delete_filme_view(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        filme.delete()
        messages.success(request, 'Filme removido com sucesso!')
        return redirect('main:home')
    return render(request, 'main/delete_filme.html', {'filme': filme})

def logout_view(request):
    logout(request)
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('main:login')

@login_required
def profile_view(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    user_filmes = Cadastro.objects.filter(user=request.user).select_related('filme')
    
    analysis_result = None
    analysis_title = ""
    analysis_type = ""

    if request.method == 'POST':
        analysis_type = request.POST.get('analysis_type')
        
        if analysis_type == 'total-filmes':
            analysis_result = user_filmes.count()
            analysis_title = "Total de Filmes Cadastrados"
        
        elif analysis_type == 'filmes-por-ano':
            analysis_result = user_filmes.values('filme__ano_lancamento').annotate(count=Count('filme__id'))
            analysis_result = {item['filme__ano_lancamento']: item['count'] for item in analysis_result}
            analysis_title = "Filmes por Ano"
        
        elif analysis_type == 'diretores-favoritos':
            analysis_result = user_filmes.values('filme__diretor').annotate(count=Count('filme__id'))
            analysis_result = {item['filme__diretor']: item['count'] for item in analysis_result}
            analysis_title = "Diretores Favoritos"

    context = {
        'perfil': perfil,
        'user_filmes': user_filmes,
        'analysis_result': analysis_result,
        'analysis_title': analysis_title,
        'analysis_type': analysis_type,
    }

    return render(request, 'main/profile.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, FilmeForm
from .models import Filme, Cadastro, Perfil
from django.contrib.auth.forms import UserCreationForm
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
def home(request):
    filmes = Filme.objects.filter(usuario=request.user)  # Assumindo que o campo no modelo Filme é 'usuario'
    return render(request, 'main/home.html', {'filmes': filmes})

@login_required
def add_filme_view(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            Cadastro.objects.create(user=request.user, filme=filme, descricao=f"Filme lançado em {filme.ano_lancamento}")
            messages.success(request, 'Filme adicionado com sucesso!')
            return redirect('main:add_filme')
    else:
        form = FilmeForm()
    
    filmes = Filme.objects.all().order_by('-id')
    
    context = {
        'form': form,
        'filmes': filmes,
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

def edit_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            messages.success(request, "Alteração realizada com sucesso!")
            return redirect('main:home')  # ou para a lista de filmes
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'edit_filme.html', {'form': form, 'filme': filme})

def delete_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        filme.delete()
        messages.success(request, "Exclusão realizada com sucesso!")
        return redirect('main:home')  # ou para a lista de filmes
    return redirect('main:edit_filme', filme_id=filme_id)

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
def profile_view(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    user_filmes = Cadastro.objects.filter(user=request.user).select_related('filme')
    
    context = {
        'perfil': perfil,
        'user_filmes': user_filmes,
    }
    return render(request, 'main/profile.html', context)


def profile_view(request):
    user = request.user
    perfil = Perfil.objects.get(user=user)
    user_filmes = perfil.filmes_favoritos.all()

    analysis_result = None
    analysis_title = ""
    analysis_type = ""

    if request.method == 'POST':
        analysis_type = request.POST.get('analysis_type')
        
        if analysis_type == 'total-filmes':
            analysis_result = user_filmes.count()
            analysis_title = "Total de Filmes Cadastrados"
        
        elif analysis_type == 'filmes-por-ano':
            analysis_result = user_filmes.values('ano_lancamento').annotate(count=Count('id'))
            analysis_result = {item['ano_lancamento']: item['count'] for item in analysis_result}
            analysis_title = "Filmes por Ano"
        
        elif analysis_type == 'diretores-favoritos':
            analysis_result = user_filmes.values('diretor').annotate(count=Count('id'))
            analysis_result = {item['diretor']: item['count'] for item in analysis_result}
            analysis_title = "Diretores Favoritos"

    context = {
        'user': user,
        'perfil': perfil,
        'user_filmes': user_filmes,
        'analysis_result': analysis_result,
        'analysis_title': analysis_title,
        'analysis_type': analysis_type,
    }

    return render(request, 'profile.html', context)




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, FilmeForm
from .models import Filme, UserFilme

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
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
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def home_view(request):
    user_filmes = UserFilme.objects.filter(usuario=request.user).select_related('filme')
    return render(request, 'main/home.html', {'user_filmes': user_filmes})

@login_required
def add_filme_view(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            UserFilme.objects.create(usuario=request.user, filme=filme)
            messages.success(request, 'Filme adicionado com sucesso!')
            return redirect('home')
    else:
        form = FilmeForm()
    return render(request, 'main/add_filme.html', {'form': form})

@login_required
def edit_filme_view(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme atualizado com sucesso!')
            return redirect('home')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'main/edit_filme.html', {'form': form, 'filme': filme})

@login_required
def delete_filme_view(request, filme_id):
    user_filme = get_object_or_404(UserFilme, filme_id=filme_id, usuario=request.user)
    if request.method == 'POST':
        user_filme.delete()
        messages.success(request, 'Filme removido com sucesso!')
        return redirect('home')
    return render(request, 'main/delete_filme.html', {'filme': user_filme.filme})

def logout_view(request):
    logout(request)
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('login')

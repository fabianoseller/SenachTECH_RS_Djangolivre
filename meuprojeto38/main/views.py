from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, FilmeForm
from .models import Filme, Cadastro



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
    cadastros = Cadastro.objects.filter(user=request.user)
    return render(request, 'main/home.html', {'cadastros': cadastros})

@login_required
def add_filme_view(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            Cadastro.objects.create(user=request.user, titulo=filme.nome, descricao=f"Filme lançado em {filme.ano_lancamento}")
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
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        filme.delete()
        messages.success(request, 'Filme removido com sucesso!')
        return redirect('home')
    return render(request, 'main/delete_filme.html', {'filme': filme})

def logout_view(request):
    logout(request)
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('login')



#  return render(request, 'main/login.html', context)
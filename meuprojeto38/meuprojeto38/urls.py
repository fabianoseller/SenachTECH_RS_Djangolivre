# meuprojeto38/main/urls.py

from django.urls import path
from . import views

app_name = 'main'  # Isso cria um namespace para as URLs desta aplicação

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('add_filme/', views.add_filme_view, name='add_filme'),
    path('edit_filme/<int:filme_id>/', views.edit_filme_view, name='edit_filme'),
    path('delete_filme/<int:filme_id>/', views.delete_filme_view, name='delete_filme'),
    path('filme/<int:filme_id>/', views.filme_detail_view, name='filme_detail'),
    path('user_filmes/', views.user_filmes_view, name='user_filmes'),
]

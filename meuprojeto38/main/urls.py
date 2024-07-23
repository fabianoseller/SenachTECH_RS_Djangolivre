from django.urls import path
from . import views  # Certifique-se de que este import está correto

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('add_filme/', views.add_filme_view, name='add_filme'),
    path('edit_filme/<int:filme_id>/', views.edit_filme_view, name='edit_filme'),
    path('delete_filme/<int:filme_id>/', views.delete_filme_view, name='delete_filme'),
    path('logout/', views.logout_view, name='logout'),
]

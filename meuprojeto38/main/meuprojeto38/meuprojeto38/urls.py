from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main import views  # Importa views do aplicativo main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='main:home'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login')
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('add_filme/', views.add_filme_view, name='add_filme'),
    path('edit_filme/<int:filme_id>/', views.edit_filme_view, name='edit_filme'),
    path('delete_filme/<int:filme_id>/', views.delete_filme_view, name='delete_filme'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),  # Adiciona uma rota para a URL raiz
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

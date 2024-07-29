from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views 
from schema_graph.views import Schema
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('', include('main.urls')),
    path('home/', views.home_view, name='home'),
    path('add_filme/', views.add_filme_view, name='add_filme'),
    path('edit_filme/<int:filme_id>/', views.edit_filme_view, name='edit_filme'),
    path('delete_filme/<int:filme_id>/', views.delete_filme_view, name='delete_filme'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),  
    path('accounts/', include('django.contrib.auth.urls')),
    path('schema/', Schema.as_view()),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

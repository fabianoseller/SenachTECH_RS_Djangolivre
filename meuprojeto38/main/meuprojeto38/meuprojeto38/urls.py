from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),  # Inclui as URLs do seu aplicativo principal com namespace 'main'
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui as URLs de autenticação padrão do Django
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
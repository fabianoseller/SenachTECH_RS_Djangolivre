from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('add-filme/', views.add_filme_view, name='add_filme'),
    path('edit-filme/<int:filme_id>/', views.edit_filme_view, name='edit_filme'),
    path('delete-filme/<int:filme_id>/', views.delete_filme_view, name='delete_filme'),
    path('logout/', views.logout_view, name='logout'),
]

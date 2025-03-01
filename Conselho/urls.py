from django.urls import path
from . import views

app_name = 'Conselho'

urlpatterns = [
    path('Inserir/', views.inserir , name='Inserir'),
    path('Listar/', views.listar, name='Listar'),
    path('Deletar/<int:pk>/', views.deletar, name='Deletar'),
    path('Editar/<int:pk>/', views.editar, name='Editar'),
    

]
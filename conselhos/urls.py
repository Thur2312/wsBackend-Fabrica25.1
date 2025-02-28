from django.urls import path
from .views import conselhoCreateView, conselhoListView, conselhoUpdateView, conselhoDeleteView


app_name = 'conselhos'

urlpatterns = [
    path('criar', conselhoCreateView.as_view(), name='criar'),
    path('Listar/', conselhoListView.as_view(), name='Listar'),
    path('Atualizar/',conselhoUpdateView.as_view(), name='Atualizar'),
    path('deleta/', conselhoDeleteView.as_view() , name='deletar'),


]
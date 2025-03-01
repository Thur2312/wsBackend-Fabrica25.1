from django.contrib import admin
from django.urls import path
from .views import  UsuarioListCreate, UsuarioRetrieveUpdateDestroy

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('traduzir/', views.Usuario, name='Texto_traduzido'),
    path('criar/', UsuarioListCreate.as_view(), name='criar/listar_tradução'),
    path('Detalhes/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view(), name='Detalhes_tradução'),
]
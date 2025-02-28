from django import forms
from .models import Conselho
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Conselho
from django.urls import reverse_lazy

class ConselhoForm(forms.ModelForm):
    class Meta:
        model: Conselho
        fields = ['nome', 'descricao']
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }
class conselhoCreateView(CreateView):
    class Meta:
        model = Conselho
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }
class conselhoListView(ListView): 
    class Meta:
        model = Conselho
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }
class conselhoUpdateView(UpdateView):
    class Meta:
        model = Conselho
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }
class conselhoDeleteView(DeleteView):
    class Meta:
        model = Conselho
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }

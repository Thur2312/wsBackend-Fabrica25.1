from django import forms
from .models import conselhos

class ConselhoForm(forms.ModelForm):
    class Meta:
        model = conselhos
        fields = ['nome', 'texto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
            'texto': 'Texto',
        }
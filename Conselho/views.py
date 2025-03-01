from django.shortcuts import render, redirect
from .models import conselhos
from .forms import ConselhoForm
from django.http import HttpResponseRedirect
import requests

# Create your views here.
def inserir(request):
    if request.method == 'POST':
        form = ConselhoForm(request.POST)
        
        conselho_digitado = request.POST['nome']
        url = f'https://api.adviceslip.com/advice/search/{conselho_digitado}'
        response = requests.get(url)
        if response.status_code == 200:
           conselho_data = response.json()
           if 'slips' in conselho_data:
               conselho = conselho['slips'][0]['advice']
           else:
               'conselho não encontrado'
        else:
            conselho = 'Erro ao buscar Conselho'
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Conselho/Listar/')
    else:
        form = ConselhoForm()
    return render(request, 'Conselho/Inserir', {'form': form})

def listar(request):
    conselho = conselhos.objects.all()
    return render(request, 'Conselho/Listar', {'conselho': conselho})

def deletar(request, id):
    conselho = conselhos.objects.get(id=id)
    conselho.delete()
    return HttpResponseRedirect('/Conselho/Listar/')

def editar(request, id):
    conselho = conselhos.objects.get(id=id)
    form = ConselhoForm(request.POST or None, instance=conselho)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Conselho/Listar/')
    return render(request, 'Conselho/Editar', {'form': form})
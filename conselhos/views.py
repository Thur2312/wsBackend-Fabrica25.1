from django.shortcuts import render
from .forms import ConselhoForm
from .models import Conselho
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


# Create your views here.

class conselhoCreateView(CreateView):
    model = Conselho
    form_class = ConselhoForm
    template_name = 'conselhos/conselho_form.html'
    success_url = '/conselhos/'

class conselhoListView(ListView):
    model = Conselho
    form_Class = ConselhoForm
    template_name = 'conselhos/conselho_list.html'
    success_url = reverse_lazy('/conselhos/')
    
class conselhoUpdateView(UpdateView):
    model = Conselho
    form_class = ConselhoForm
    template_name = 'conselhos/conselho_form.html'
    success_url = reverse_lazy('/conselhos/')

class conselhoDeleteView(DeleteView):
    model = Conselho
    template_name = 'conselhos/conselho_delete.html'
    success_url = reverse_lazy('/conselhos/')
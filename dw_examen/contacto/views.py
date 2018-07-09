from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacto
from django.template import loader
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'contacto/index.html'
    model = Contacto
    context_object_name = 'contactos'


class DetailView(generic.DetailView):
    model = Contacto
    template_name = 'contacto/detail.html'
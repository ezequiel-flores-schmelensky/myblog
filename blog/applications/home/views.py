import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from applications.entrada.models import Entry
from applications.home.models import Home

from django.views.generic import (
    TemplateView,
    CreateView
)
# form
from .forms import SubscribersForm


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # contexto de home
        context["home"] = Home.objects.latest('created')
        # contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # enviamos formulario de suscripcion
        context["form"] = SubscribersForm
        return context
    


class SuscriberCreateView(CreateView):
    form_class = SubscribersForm
    success_url = '.'
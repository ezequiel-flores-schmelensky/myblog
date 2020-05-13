import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from applications.entrada.models import Entry

from django.views.generic import (
    TemplateView
)


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        return context
    

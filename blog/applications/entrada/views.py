from django.shortcuts import render
from django.views.generic import (
    ListView
)


class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 10

    def get_queryset(self):
        
        return[]

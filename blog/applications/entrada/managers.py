from django.db import models


class EntryManager(models.Manager):

    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created').first()

    def entradas_en_home(self):
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]
    
    def entradas_recientes(self):
        return self.filter(
            public=True,
        ).order_by('-created')[:6]
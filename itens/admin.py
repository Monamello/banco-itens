from django.contrib import admin
from .models import Item, Alternativa, Cursos, UnidadeCurricular

# Register your models here.
admin.site.register(Item)
admin.site.register(Alternativa)
admin.site.register(Cursos)
admin.site.register(UnidadeCurricular)

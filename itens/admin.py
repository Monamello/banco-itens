from django.contrib import admin
from .models import Item, Alternativa, Cursos, UnidadeCurricular
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


# Register your models here.
admin.site.register(Item)
admin.site.register(Alternativa)
admin.site.register(Cursos)
admin.site.register(UnidadeCurricular)
admin.site.site_header = 'CU'
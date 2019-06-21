from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import ItensViewSet, AlternativasViewSet


router = routers.DefaultRouter()
router.register(r'itens', ItensViewSet, base_name='Itens')
router.register(r'alternativas', AlternativasViewSet, base_name='Alternativas')

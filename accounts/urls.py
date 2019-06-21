from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from django.views.generic.base import TemplateView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='Users')
router.register(r'groups', GroupViewSet, base_name='Groups')

urlpatterns = [
    path('accounts/login/', UserViewSet, name='users'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

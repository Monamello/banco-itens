from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

#router = routers.DefaultRouter()

urlpatterns = [
    #path('accounts/login/', UserViewSet, name='users'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

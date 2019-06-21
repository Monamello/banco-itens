from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from itens.views import ItensViewSet, AlternativasViewSet
from accounts.views import UserViewSet, GroupViewSet
from django.views.generic.base import TemplateView
from . import routers
from accounts.urls import router as accounts
from itens.urls import router as itens


router = routers.DefaultRouter()
router.extend(accounts)
router.extend(itens)

urlpatterns = [
    path('', include(router.urls)),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('itens/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

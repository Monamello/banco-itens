from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from .views import ItensViewSet, ItemListView, MyItemListView, ItemCreateView, AlternativaCreateView,AlternativasViewSet


router = routers.DefaultRouter()
router.register(r'itens', ItensViewSet, base_name='Itens')
router.register(r'alternativas', AlternativasViewSet, base_name='Alternativas')
urlpatterns = router.urls

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('meus-itens', MyItemListView.as_view(), name='my_item_list'),
    path('item/create/', ItemCreateView.as_view(), name='item_create'),
    path('alternativas/create/', AlternativaCreateView.as_view(), name='alternativa_create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

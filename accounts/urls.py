from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, list_users


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='Users')
router.register(r'groups', GroupViewSet, base_name='Groups')

urlpatterns = [
    path('accounts/login/', UserViewSet, name='login'),
    path('accounts/logout/', UserViewSet, name='logout'),
    path('accounts/password_change/', UserViewSet, name='password_change'),
    path('accounts/password_change/done/', UserViewSet, name='password_change_done'),
    path('list', list_users, name='list_docentes'),
    path('accounts/password_reset/', UserViewSet, name='password_reset'),
    path('accounts/password_reset/done/', UserViewSet, name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', UserViewSet, name='password_reset_confirm'),
    path('accounts/reset/done/', UserViewSet, name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

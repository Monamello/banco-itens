from .models import Item, Alternativa
from .serializers import ItensSerializer, AlternativasSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ItensViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItensSerializer

    def post(self, request):
        self.serializer_class.save(autor=request.user)

    
class AlternativasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Alternativa.objects.all()
    serializer_class = AlternativasSerializer
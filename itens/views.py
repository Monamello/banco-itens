from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets

from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render


from .models import Item, Alternativa
from .serializers import ItensSerializer, AlternativasSerializer
from .forms import ItemForm, AlternativaForm


class ItensViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItensSerializer
    template_name = 'itens/itens_form.html'

    def post(self, request):
        self.serializer_class.save(autor=request.user)


class ItemListView(ListView):
    model = Item
    template_name = 'itens/item_list.html'

    def get(self, request, *args, **kwargs):
        itens = self.model.objects.all()
        return render(request, self.template_name, {'itens': itens})


# def list_users(request):
#     users = User.objects.all().order_by('-date_joined')
#     context = {'users': users}
#     return render(request, 'users.html', context)



class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'itens/item_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/alternativas/create/')


class AlternativaCreateView(CreateView):
# The view itens.views.AlternativaCreateView didn't return an HttpResponse object. It returned None instead.

    model = Alternativa
    form_class = AlternativaForm
    template_name = 'itens/item_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # self.serializer_class.save(item=item.pk)
        if form.is_valid():
            #dá erro quando retorna pela segunda vez aqui
            return HttpResponseRedirect('/item/list/')


class AlternativasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Alternativa.objects.all()
    serializer_class = AlternativasSerializer

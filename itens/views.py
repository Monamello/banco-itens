from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets

from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

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
        itens = self.get_queryset()
        return render(request, self.template_name, {'itens': itens})

    def get_queryset(self):
        query = self.request.GET.get('q')
        filter = Item.objects.filter(Q(cursos__docente=self.request.user))
        if query:
            object_list = filter.filter(
                Q(enunciado__icontains=query) | Q(comando__icontains=query) | 
                Q(suporte_texto__icontains=query) | Q(dificuldade__icontains=query) |
                Q(cursos__nome__icontains=query) | Q(unidades_curriculares__nome__icontains=query)
            )
        else:
            object_list = filter.all()                
        return object_list
 

# def list_users(request):
#     users = User.objects.all().order_by('-date_joined')
#     context = {'users': users}
#     return render(request, 'users.html', context)



class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    form_alternativa = AlternativaForm
    serializer_class = ItensSerializer
    serializer = AlternativasSerializer
    template_name = 'itens/item_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        form_alt = self.form_alternativa(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'form_alt': form_alt, 'range': range(1, 6)})
      
     
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.autor = request.user
        form_alt = self.form_alternativa(request.POST)
        if form.is_valid() and form_alt.is_valid():
            form.save()
            form_alt.instance.item = form.instance
            form_alt.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect('/')


    def get_success_url(self):
        return reverse('item_list')


class AlternativaCreateView(CreateView):
    model = Alternativa
    form_class = AlternativaForm
    template_name = 'itens/item_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/item/list/')


class AlternativasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Alternativa.objects.all()
    serializer_class = AlternativasSerializer

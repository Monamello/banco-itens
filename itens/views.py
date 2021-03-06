from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets

from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from .models import Item, Alternativa, Cursos, UnidadeCurricular
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
        try:
            user_is_authenticated = request.user.is_authenticated()
        except TypeError:
            user_is_authenticated = request.user.is_authenticated

        if user_is_authenticated:
            itens = self.get_queryset()
        else:
            itens = self.model.objects.all()
        title = "Itens"
        return render(request, self.template_name, {'itens': itens, 'title' : title, 'isMyItens' : False})


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


class MyItemListView(ListView):
    model = Item
    template_name = 'itens/item_list.html'


    def get(self, request, *args, **kwargs):
        try:
            user_is_authenticated = request.user.is_authenticated()
        except TypeError:
            user_is_authenticated = request.user.is_authenticated

        if user_is_authenticated:
            itens = self.get_queryset(request)
        else:
            itens = self.model.objects.all().filter(autor=request.user)
        #itens = self.model.objects.all().filter(autor=request.user)
        title = "Meus Itens"
        return render(request, self.template_name, {'itens': itens, 'title' : title, 'isMyItens' : True})

    def get_queryset(self,request):
        query = self.request.GET.get('q')
        filter = self.model.objects.all().filter(autor=request.user)
        if query:
            object_list = filter.filter(
                Q(enunciado__icontains=query) | Q(comando__icontains=query) |
                Q(suporte_texto__icontains=query) | Q(dificuldade__icontains=query) |
                Q(cursos__nome__icontains=query) | Q(unidades_curriculares__nome__icontains=query)
            )
        else:
            object_list = filter.all()
        return object_list


def sucess_create(request):
    return render(request, 'success.html')


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    form_alternativa = AlternativaForm
    serializer_class = ItensSerializer
    serializer = AlternativasSerializer
    template_name = 'itens/item_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        form.fields['cursos'].queryset = Cursos.objects.filter(docente=self.request.user)
        form.fields['unidades_curriculares'].queryset = UnidadeCurricular.objects.filter(Q(cursos__docente=self.request.user))
        alternativas = ['A','B', 'C', 'D','E']
        return render(request, self.template_name, {'form': form,'alternativas': alternativas})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        form.instance.autor = request.user
        forms_alt = []
        is_valid_forms_alt = []
        for i in range(1,6):
            post = {
                "texto": request.POST.get('texto' + str(i), ''),
                "correta": request.POST.get("correta" + str(i), 'off') == 'on'
            }
            form_alt = self.form_alternativa(post, {"imagem": request.FILES.get("imagem"+str(i), [])})
            forms_alt.append(form_alt)
            is_valid_forms_alt.append(form_alt.is_valid())

        if form.is_valid() and all(is_valid_forms_alt):
            form.save()
            for form_alt in forms_alt:
                form_alt.instance.item = form.instance
                form_alt.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


    def get_success_url(self):
        return reverse('sucess_form_create')


class AlternativaCreateView(CreateView):
    model = Alternativa
    form_class = AlternativaForm
    template_name = 'itens/item_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/item/list/')


class AlternativasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Alternativa.objects.all()
    serializer_class = AlternativasSerializer

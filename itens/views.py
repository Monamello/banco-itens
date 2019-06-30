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
        itens = self.model.objects.all()
        return render(request, self.template_name, {'itens': itens})


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
        form.fields['cursos'].queryset = Cursos.objects.filter(docente=self.request.user)
        form.fields['unidades_curriculares'].queryset = UnidadeCurricular.objects.filter(Q(cursos__docente=self.request.user))
        return render(request, self.template_name, {'form': form})
      
     
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

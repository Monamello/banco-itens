from django import forms
from django.forms import ModelForm
from .choices import DIFICULDADES
from .models import Item, Cursos, UnidadeCurricular, Alternativa


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('autor', )

    # enunciado = forms.CharField(widget=forms.Textarea)
    # suporte = forms.CharField(widget=forms.Textarea)
    # suporte_imagem = forms.ImageField(required=False, label='Suporte Imagem')
    # comando = forms.CharField(widget=forms.Textarea)
    # dificuldade = forms.ChoiceField(choices=DIFICULDADES, label="Dificuldade", widget=forms.Select())
    # cursos = forms.MultipleChoiceField(
    #     choices=[(choice.pk, choice.nome) for choice in Cursos.objects.all()],
    #     label='Curso', widget=forms.SelectMultiple())
    # unidades_curriculares = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
    #                                             queryset=UnidadeCurricular.objects.all())



class AlternativaForm(forms.ModelForm):
    class Meta:
        model = Alternativa
        exclude = ('item',)

    texto = forms.CharField(widget=forms.Textarea, required=False)
    imagem = forms.ImageField(required=False)
    correta = forms.BooleanField(required=False)

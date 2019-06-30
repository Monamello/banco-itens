from django import forms
from django.forms import ModelForm
from .choices import DIFICULDADES
from .models import Item, Cursos, UnidadeCurricular, Alternativa


class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ()

    enunciado = forms.CharField(widget=forms.Textarea)
    suporte = forms.CharField(widget=forms.Textarea)
    suporte_imagem = forms.ImageField(required=False, label='Suporte Imagem')
    comando = forms.CharField(widget=forms.Textarea)
    dificuldade = forms.ChoiceField(choices=DIFICULDADES, label="Dificuldade", widget=forms.Select())
    cursos = forms.MultipleChoiceField(
        choices=[(choice.pk, choice.nome) for choice in Cursos.objects.all()],
        label='Curso', widget=forms.SelectMultiple())
    unidades_curriculares = forms.MultipleChoiceField(
        choices=[(choice.pk, choice.nome) for choice in UnidadeCurricular.objects.all()],
        label='Curso', widget=forms.SelectMultiple())


class AlternativaForm(ModelForm):
    class Meta:
        model = Alternativa
        exclude = ()

    texto = forms.CharField(widget=forms.Textarea)
    imagem = forms.ImageField(required=False)
    correta = forms.BooleanField()

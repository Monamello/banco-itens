from django import forms
from .choices import DIFICULDADES
from .models import Item, Cursos, UnidadeCurricular, Alternativa


class ItemForm(forms.Form):
    enunciado = forms.CharField(widget=forms.Textarea)
    suporte = forms.CharField(widget=forms.Textarea)
    comando = forms.CharField(widget=forms.Textarea)
    dificuldade = forms.ChoiceField(choices=DIFICULDADES, label="Dificuldade", widget=forms.Select())
    cursos = forms.MultipleChoiceField(
        choices=[(choice.pk, choice.nome) for choice in Cursos.objects.all()],
        label='Curso', widget=forms.SelectMultiple())
    unidades_curriculares = forms.MultipleChoiceField(
        choices=[(choice.pk, choice.nome) for choice in UnidadeCurricular.objects.all()],
        label='Curso', widget=forms.SelectMultiple())


class AlternativaForm(forms.Form):
    texto = forms.CharField(widget=forms.Textarea)
    imagem = forms.ImageField()
    correta = forms.BooleanField()
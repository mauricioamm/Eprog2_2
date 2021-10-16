from django.forms import ModelForm, Textarea
from django import forms

from .models import EprogModel, CalculosModel, SessaoModel, ProcedimentoModel

class EprogForm(forms.ModelForm):
    class Meta:
        model = EprogModel
        fields = ['id', 'Participante', 'Ordem', 'Topico', 'Textao', 'SuaResposta', 'OndeFigura1',
                  'OndeFigura2', 'DuvidaComent',
                  'Acertou', 'Jafoi', 'Ativada', 'Corretas', 'Porcentagem',
                  'Marcador1', 'Marcador2', 'Marcador3', 'Marcador4', 'Marcador5']
        widgets = {
            'Topico': forms.TextInput(attrs={'size': 150}),
            'Textao': forms.TextInput(attrs={'size': 150}),
            'OndeFigura1': forms.TextInput(attrs={'size': 100}),
            'OndeFigura2': forms.TextInput(attrs={'size': 100}),
            'SuaResposta': forms.TextInput(attrs={'size': 100}),
            'DuvidaComent': forms.TextInput(attrs={'size': 100}),
            'Marcador1': forms.TextInput(attrs={'size': 100}),
            'Marcador2': forms.TextInput(attrs={'size': 100}),
            'Marcador3': forms.TextInput(attrs={'size': 100}),
            'Marcador4': forms.TextInput(attrs={'size': 100}),
            'Marcador5': forms.TextInput(attrs={'size': 100}),
        }

class CalculosForm(forms.ModelForm):
    class Meta:
        model = CalculosModel
        fields = ['id', 'Porcentagem', 'Corretas', 'Incorretas', 'Ordem']
        widgets = {
        }


class SessaoForm(forms.ModelForm):
    class Meta:
        model = SessaoModel
        fields = ['id', 'Participante', 'Modulo', 'Sessao', 'Dia',
                  'Horario', 'Tentativa', 'Topico', 'DuvidaComent', 'Acertou']

        widgets = {
            'id': forms.TextInput(attrs={'size': 5}),
            'Participante': forms.TextInput(attrs={'size': 100}),
            'Modulo': forms.TextInput(attrs={'size': 5}),
            'Sessao': forms.TextInput(attrs={'size':  5}),
            'Dia': forms.TextInput(attrs={'size': 20}),
            'Horario': forms.TextInput(attrs={'size': 20}),
            'Tentativa': forms.TextInput(attrs={'size': 20}),
            'Topico': forms.TextInput(attrs={'size': 100}),
            'DuvidaComent': forms.TextInput(attrs={'size': 100}),
            'Acertou': forms.TextInput(attrs={'size': 5})
        }

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = ProcedimentoModel
        fields = ['id', 'Participante', 'Banco', 'NomeCompleto', 'Idade',
                  'Acesso', 'Botao_avalia', 'SessaoAtual']
        widgets = {
            'id': forms.TextInput(attrs={'size': 5}),
            'Participante': forms.TextInput(attrs={'size': 50}),
            'Banco': forms.TextInput(attrs={'size': 50}),
            'NomeCompleto': forms.TextInput(attrs={'size': 50}),
            'Idade': forms.TextInput(attrs={'size': 5}),
            'Acesso': forms.TextInput(attrs={'size': 5}),
            'Botao_avalia': forms.TextInput(attrs={'size': 5}),
            'SessaoAtual': forms.TextInput(attrs={'size': 5}),

        }

class ImageForm2(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = EprogModel
        fields = ['id', 'Participante', 'Ordem', 'Topico', 'Textao', 'SuaResposta', 'OndeFigura1',
                  'OndeFigura2', 'DuvidaComent',
                  'Acertou', 'Jafoi', 'Ativada', 'Corretas', 'Porcentagem',
                  'Marcador1', 'Marcador2', 'Marcador3', 'Marcador4', 'Marcador5',
                  'title', 'image']
        widgets = {
            'Topico': forms.TextInput(attrs={'size': 150}),
            'Textao': forms.TextInput(attrs={'size': 150}),
            'OndeFigura1': forms.TextInput(attrs={'size': 100}),
            'OndeFigura2': forms.TextInput(attrs={'size': 100}),
            'SuaResposta': forms.TextInput(attrs={'size': 100}),
            'DuvidaComent': forms.TextInput(attrs={'size': 100}),
            'Marcador1': forms.TextInput(attrs={'size': 100}),
            'Marcador2': forms.TextInput(attrs={'size': 100}),
            'Marcador3': forms.TextInput(attrs={'size': 100}),
            'Marcador4': forms.TextInput(attrs={'size': 100}),
            'Marcador5': forms.TextInput(attrs={'size': 100}),
        }

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = EprogModel
        fields = ('title', 'image')


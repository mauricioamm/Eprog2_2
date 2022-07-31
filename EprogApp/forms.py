from django.forms import ModelForm, Textarea
from django import forms

from .models import EprogModel, CalculosModel, SessaoModel, ProcedimentoModel, PretesteModel, PostesteModel, ModulosModel

class EprogForm(forms.ModelForm):
    class Meta:
        model = EprogModel
        fields = ['id', 'Participante', 'Ordem','Modulo','Topico', 'Textao', 'SuaResposta', 'OndeFigura1',
                  'OndeFigura2', 'DuvidaComent',
                  'Acertou', 'Jafoi', 'Ativada', 'Corretas', 'Porcentagem',
                  #'Marcador1', 'Marcador2', 'Marcador3', 'Marcador4', 'Marcador5'
                  ]
        widgets = {
            'Topico': forms.Textarea(attrs={'rows': 5, 'cols': 150}),
            'Textao': forms.Textarea(attrs={'rows': 5, 'cols': 150}),
            'OndeFigura1': forms.TextInput(attrs={'size': 100}),
            'OndeFigura2': forms.TextInput(attrs={'size': 100}),
            'SuaResposta': forms.TextInput(attrs={'size': 100}),
            'DuvidaComent': forms.TextInput(attrs={'size': 100}),
            #'Marcador1': forms.TextInput(attrs={'size': 100}),
            #'Marcador2': forms.TextInput(attrs={'size': 100}),
            #'Marcador3': forms.TextInput(attrs={'size': 100}),
            #'Marcador4': forms.TextInput(attrs={'size': 100}),
            #'Marcador5': forms.TextInput(attrs={'size': 100}),
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
        fields = ['id', 'Participante', 'Banco', 'NomeCompleto', 'Idade', 'Condicao', 'EtapaAtual',
                  'Acesso', 'Botao_avalia', 'SessaoAtual', 'ModuloAtual', 'ModuloAntigo', 'ModuloFinal', 'Retreino'
                  ]

        widgets = {
            'id': forms.TextInput(attrs={'size': 5}),
            'Participante': forms.TextInput(attrs={'size': 50}),
            'Banco': forms.TextInput(attrs={'size': 50}),
            'NomeCompleto': forms.TextInput(attrs={'size': 50}),
            'Idade': forms.TextInput(attrs={'size': 5}),
            'Acesso': forms.TextInput(attrs={'size': 5}),
            'Condicao': forms.TextInput(attrs={'size': 5}),
            'FimEstudo': forms.TextInput(attrs={'size': 5}),
            'FimUltimoModulo': forms.TextInput(attrs={'size': 5}),
            'Botao_avalia': forms.TextInput(attrs={'size': 5}),
            'SessaoAtual': forms.TextInput(attrs={'size': 5}),
            'ModuloAtual= ': forms.TextInput(attrs={'size': 5}),
            'ModuloAntigo': forms.TextInput(attrs={'size': 5}),
            'ModuloFinal': forms.TextInput(attrs={'size': 5}),
            'Retreino': forms.TextInput(attrs={'size': 5}),
            'EtapaAtual': forms.TextInput(attrs={'size': 30}),
        }

class Entrada_ExperimentadorForm(forms.ModelForm):
    class Meta:
        model = ProcedimentoModel
        fields = ['Senha_Salva']
        #fields = ['Senha_Experimentador', 'Senha_Salva']

        widgets = {
            #'Senha_Experimentador': forms.TextInput(attrs={'size': 50}),
            'Senha_Salva': forms.TextInput(attrs={'size': 50, 'label': ''})
            }

class Editar_ModulosForm(forms.ModelForm):
    class Meta:
        model = ModulosModel
        fields = ['id',
                  'NoModulo',
                  'Ordem',
                  'Descricao',
                  'Treino_Primeiro',
                  'Treino_Ultimo',
                  'PreTeste_Primeiro',
                  'PreTeste_Ultimo',
                  'TemPosTeste',
                  'PosTeste_Primeiro',
                  'PosTeste_Ultimo',
                  'Treino_Acesso',
                  'PreTeste_Acesso',
                  'PosTeste_Acesso',
                  'Modulo_EtapaAtual',
                  'Delineamento'
                  ]

        widgets = {
            'id': forms.TextInput(attrs={'size': 5}),
            'NoModulo'          : forms.TextInput(attrs={'size': 5}),
            'Ordem'             : forms.NumberInput(attrs={'size': 5}),
            'Descricao'         : forms.TextInput(attrs={'size': 100}),
            'Treino_Primeiro'   : forms.NumberInput(attrs={'size': 5}),
            'Treino_Ultimo'     : forms.NumberInput(attrs={'size': 5}),
            'PreTeste_Primeiro' : forms.NumberInput(attrs={'size': 5}),
            'PreTeste_Ultimo'   : forms.NumberInput(attrs={'size': 5}),
            'TemPosTeste'       : forms.NumberInput(attrs={'size': 5}),
            'PosTeste_Primeiro' : forms.NumberInput(attrs={'size': 5}),
            'PosTeste_Ultimo'   : forms.NumberInput(attrs={'size': 5}),
            'Treino_Acesso'     : forms.TextInput(attrs={'size': 5}),
            'PreTeste_Acesso'   : forms.TextInput(attrs={'size': 5}),
            'PosTeste_Acesso'   : forms.TextInput(attrs={'size': 5}),
            'Modulo_EtapaAtual' : forms.TextInput(attrs={'size': 5}),
            'Participante': forms.TextInput(attrs={'size': 50}),
            'Delineamento': forms.TextInput(attrs={'size': 5}),
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

class PretesteForm(forms.ModelForm):
    class Meta:
        model = PretesteModel
        fields = ['Ordem', 'Modulo', 'Acertou', 'Jafoi', 'Questao',
                  'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E', 'Escolheu']

        """
        ESCOLHAS = [('a)','Alternativa_A'),
                   ('letra B', 'Alternativa_B'),
                   ('letra C', 'Alternativa_C'),
                   ('letra D', 'letra D'),
                   ('letra E', 'letra E')]

        #escolher = forms.ChoiceField(choices=ESCOLHAS, widget=forms.RadioSelect)
        """
        preteste_listinha = ('a)',
                             'b)',
                             'c)',
                             'd)',
                             'e)',
                             )

        Escolheu = forms.ChoiceField(widget=forms.RadioSelect(), choices=preteste_listinha)
        """"
        widgets = {
            'Ordem': forms.TextInput(attrs={'size': 5}),
            'Modulo': forms.TextInput(attrs={'size': 5}),
            'Acertou': forms.TextInput(attrs={'size': 5}),
            'Jafoi': forms.TextInput(attrs={'size': 5}),
            'Questao': forms.TextInput(attrs={'size': 150}),
            'Alternativa_A': forms.RadioSelect,
            'Alternativa_B': forms.RadioSelect,
            'Alternativa_C': forms.RadioSelect,
            'Alternativa_D': forms.TextInput(attrs={'size': 150}),
            'Alternativa_E': forms.TextInput(attrs={'size': 150}),

        }
        """

class PretesteForm2(forms.ModelForm):
    class Meta:
        model = PretesteModel
        fields = ['Ordem', 'Modulo', 'Acertou', 'Jafoi', 'Questao',
                  'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E', 'Escolheu']

        widgets = {
            'Ordem': forms.TextInput(attrs={'size': 5}),
            'Modulo': forms.TextInput(attrs={'size': 5}),
            'Acertou': forms.TextInput(attrs={'size': 5}),
            'Jafoi': forms.TextInput(attrs={'size': 5}),
            'Questao': forms.Textarea(attrs={'rows': 5, 'cols': 150}),
            'Alternativa_A': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_B': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_C': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_D': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_E': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Escolheu': forms.TextInput(attrs={'size': 5}),
        }

class PretesteForm_executar(forms.ModelForm):
    class Meta:
        model = PretesteModel
        fields = ['Ordem', 'Modulo', 'Acertou', 'Jafoi', 'Questao',
                  'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E', 'Escolheu']

        widgets = {
            'Ordem': forms.TextInput(attrs={'size': 5}),
            'Modulo': forms.TextInput(attrs={'size': 5}),
            'Acertou': forms.TextInput(attrs={'size': 5}),
            'Jafoi': forms.TextInput(attrs={'size': 5}),
            'Questao': forms.Textarea(attrs={'rows': 5, 'cols': 150}),
            'Alternativa_A': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_B': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_C': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_D': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_E': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Escolheu': forms.TextInput(attrs={'size': 5}),
        }



class PostesteForm(forms.ModelForm):
    class Meta:
        model = PostesteModel
        fields = ['Ordem', 'Modulo', 'Acertou', 'Jafoi', 'Questao',
                  'Alternativa_A', 'Alternativa_B', 'Alternativa_C', 'Alternativa_D', 'Alternativa_E', 'Escolheu']

        widgets = {
            'Ordem': forms.TextInput(attrs={'size': 5}),
            'Modulo': forms.TextInput(attrs={'size': 5}),
            'Acertou': forms.TextInput(attrs={'size': 5}),
            'Jafoi': forms.TextInput(attrs={'size': 5}),
            'Questao': forms.Textarea(attrs={'rows': 5, 'cols': 150}),
            'Alternativa_A': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_B': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_C': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_D': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Alternativa_E': forms.Textarea(attrs={'rows': 1, 'cols': 140}),
            'Escolheu': forms.TextInput(attrs={'size': 5}),
        }
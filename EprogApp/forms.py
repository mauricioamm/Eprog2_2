from django.forms import ModelForm, Textarea
from django import forms

from .models import EprogModel, CalculosModel

#class EprogForm(ModelForm):
class EprogForm(forms.ModelForm):
    class Meta:
        model = EprogModel
        fields = ['id', 'Participante', 'Ordem', 'Topico', 'Textao', 'SuaResposta', 'OndeFigura1', 'OndeFigura2', 'DuvidaComent',
                  'Acertou', 'Jafoi', 'Ativada', 'Corretas', 'Porcentagem',
                  'Marcador1', 'Marcador2', 'Marcador3', 'Marcador4', 'Marcador5']
        widgets = {
                   'id': forms.TextInput(attrs={'size': 3}),
                   'Participante': forms.TextInput(attrs={'size': 70}),
                   'Ordem': forms.TextInput(attrs={'size': 3}),
                   'Topico': forms.TextInput(attrs={'size': 70}),
                   'Textao': forms.TextInput(attrs={'size': 70}),
                   'SuaResposta': forms.TextInput(attrs={'size': 70}),
                   'OndeFigura1': forms.TextInput(attrs={'size': 70}),
                   'OndeFigura2': forms.TextInput(attrs={'size': 70}),
                   'DuvidaComent': forms.TextInput(attrs={'size': 70}),
                   'Acertou': forms.TextInput(attrs={'size': 3}),
                   'Jafoi': forms.TextInput(attrs={'size': 3}),
                   'Ativada': forms.TextInput(attrs={'size': 3}),
                   'Corretas': forms.TextInput(attrs={'size': 3}),
                   'Porcentagem': forms.TextInput(attrs={'size': 3}),
                   'Marcador1': forms.TextInput(attrs={'size': 70}),
                   'Marcador2': forms.TextInput(attrs={'size': 70}),
                   'Marcador3': forms.TextInput(attrs={'size': 70}),
                   'Marcador4': forms.TextInput(attrs={'size': 70}),
                   'Marcador5': forms.TextInput(attrs={'size': 70}),
                   'corretas': forms.TextInput(attrs={'size': 70})
                   #'corretas':forms.CharField(max_length=20, initial='999')
                  }

class CalculosForm(forms.ModelForm):
            model= CalculosModel
            Porcentagem = forms.IntegerField(initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'input'})),
            Corretas = forms.IntegerField(initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'input'})),
            Incorretas = forms.IntegerField(initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'input'})),
            Campo4 = forms.IntegerField(initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'input'})),
            Campo5 = forms.IntegerField(initial=0, min_value=0, widget=forms.NumberInput(attrs={'class': 'input'})),


            #fields = ['Porcentagem', 'Corretas', 'Incorretas', 'Campo4',
            #          'Campo5']
            #widgets = {
            #    'Porcentagem': forms.NumberInput(required=False, attrs={'size:4', 'value:0'}),
            #    'Corretas': forms.NumberInput(attrs={'size:4', 'value:0'}),
            #    'Incorretas': forms.NumberInput(attrs={'size:4', 'value:0'}),
            #    'Campo4': forms.NumberInput(attrs={'size:4', 'value:0'}),
            #    'Campo5': forms.NumberInput(attrs={'size:4', 'value':'0'}),
            #}

            # .IntegerField(attrs={initial:'999'}),
            #'Corretas': forms.TextInput(attrs={'size': 70}),
            #           'Incorretas': forms.TextInput(attrs={'size': 70}),
            #           'Campo4': forms.TextInput(attrs={'size': 70}),
            #           'Campo5': forms.TextInput(attrs={'size': 70}),
            #           # 'corretas':forms.CharField(max_length=20, initial='999')
            #Porcentagem = forms.IntegerField(max_length=3, blank=True, null=True)
            #Corretas = forms.IntegerField(max_length=3, blank=True, null=True)
            #Incorretas = forms.IntegerField(max_length=3, blank=True, null=True)
            #Campo4 = forms.IntegerField(max_length=3, blank=True, null=True)
            #Campo5 = forms.IntegerField(max_length=3, blank=True, null=True)
            #class Form2(forms.Form):
            #    campo_a = forms.CharField(max_length=20, initial='999', required=False)
            # corretas= forms.TextInput(attrs={'size': 70}),
            # incorretas = forms.TextInput(attrs={'size': 70}),
            # corretas= forms.CharField(required=False, initial='5'),
            # incorretas = forms.CharField(required=False, initial='5'),


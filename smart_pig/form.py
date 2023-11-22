from django import forms
from smart_pig.models import Porco


class CadastroPorco(forms.ModelForm):

    class Meta:
        model = Porco
        fields = ('data_nas', 'peso', 'sexo', 'reprodutivo',
                  'vacinas', 'medicamentos', 'pai', 'mae')
        widgets = {
            'data_nas': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite o a data de nascimento'}
            ),
            'peso': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite o peso'}
            ),

            'vacinas': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite o as vacinas'}
            ),
            'medicamentos': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite o os medicamentos'}
            ),
            'pai': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite o nome do pai'}
            ),
            'mae': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite o nome da mãe'}
            )

        }

from django import forms
from .models import Cadastro, MensagensSuporte

# forms.py
from django import forms
from .models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']


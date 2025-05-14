from django import forms
from models import ConsultaCNPJ

class ConsultaCNPJform(forms.ModelForm):
    class Meta:
        model = ConsultaCNPJ
        fields = ['cnpj']
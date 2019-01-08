from django import forms
from .models import Servidor
class ServerCreationForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ("name","ipAddr","password",)

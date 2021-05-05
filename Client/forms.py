from django import forms
from .models import Clients
from django.forms import widgets

class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['nom', 'prenom','email','telephone','date_souscription', 'situation']
        widgets= {'date_souscription' : widgets.SelectDateWidget}
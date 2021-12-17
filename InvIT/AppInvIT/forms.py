from django import forms
from django.db.models.fields import NullBooleanField

class NotebookFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    numeroSerie = forms.CharField()

class DesktopFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    numeroSerie = forms.CharField()
    
class ServerFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    numeroSerie = forms.CharField()
    esRackeable = forms.NullBooleanField()

class StorageFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    numeroSerie = forms.CharField()
    almacenamiento = forms.IntegerField()
    esRackeable = forms.NullBooleanField()
from django import forms

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
    esRackeable = forms.BooleanField()

class StorageFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    numeroSerie = forms.CharField()
    almacenamiento = forms.IntegerField()
    esRackeable = forms.BooleanField()
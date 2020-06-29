from django import forms

class PhotoForm(forms.Form):
    nom = forms.CharField(max_length=100)
    photo = forms.ImageField()

class NomForm(forms.Form):
    nom = forms.CharField(max_length=100)

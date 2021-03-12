from django import forms

class UploadForm(forms.Form):
   nm = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Public name'}))
   des = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'About this File or Author'}))
   tgs = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'#Tags ex:- #2020 #Nani #Lol'}))
   flnm = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','accept':'audio/*'}))
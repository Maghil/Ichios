from django import forms

class UploadForm(forms.Form):
   name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Public name'}))
   description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'About this File or Author'}))
   tags = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'#Tags ex:- #2020 #Nani #Lol'}))
   filename = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','accept':'audio/*'}))
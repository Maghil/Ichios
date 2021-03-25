from django import forms
from homepage.fields import RestrictedFileField
class UploadForm(forms.Form):
   name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Public name'}))
   description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'About this File or Author'}))
   tags = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'#Tags ex:- #2020 #Nani #Lol'}))
  ## filename = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','accept':'.mp3','id':'file'}))
   filename = RestrictedFileField(accept="audio/wav",max_upload_size=2097152) 


class SearchForm(forms.Form):
   search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search for Name or Tags '}))

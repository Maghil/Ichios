from django import forms
from homepage.fields import RestrictedFileField
class UploadForm(forms.Form):
   name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Public name','id':'name'}))
   description = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'About this File or Author','id':'desc'}))
   tags = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'seperate tags by space','id':'tags'}))
   filename = RestrictedFileField(accept="audio/wav",max_upload_size=2097152) 


class SearchForm(forms.Form):
   search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search for Name or Tags '}))

class report_form(forms.Form):
   hash_value = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Report','id':'hvtxt','style':'display:none; '}))
   name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Report','id':'nmtxt','style':'display:none; '}))
   reason = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Report reason here...!','id':'retxt','style':'width:50%;'}))
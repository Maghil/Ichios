from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),label="")
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username','style':'margin-top:50px;'}),label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-type Password'}),label="")
    class Meta:
        model = User
        fields =['username','email','password1','password2']

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username','style':'margin-top:50px;'}),label="")
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label="")


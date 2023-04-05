from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'tipe':'text','placeholder':'NickName...'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'tipe':'text','placeholder':'First Name...'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'tipe':'text','placeholder':'Last Name...'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'tipe':'email','placeholder':'Email...'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'id':'pass','tipe':'password','placeholder':'password...'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'id':'pass2','tipe':'password','placeholder':'Password Check...'}))
    
    class Meta:
        model = User
        fields= ('username','first_name','last_name','email','password1','password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'tipe':'text','placeholder':'NickName...'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'id':'pass','tipe':'password','placeholder':'password...'}))

    class Meta:
        model = User
        fields= ('username','password',)

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={}))
    email = forms.CharField(widget=forms.TextInput(attrs={}))
    image = forms.ImageField(widget=forms.TextInput(attrs={}))
    
    class Meta:
        model = User
        fields= ('username','first_name','last_name','email','image')

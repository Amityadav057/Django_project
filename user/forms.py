from django.contrib.auth.models import User
from django import forms
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    class Meta:
        model = User
        fields =['username','password','first_name','last_name','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Fname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
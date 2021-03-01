from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    display_name= forms.CharField(max_length=50)
    email = forms.EmailField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)